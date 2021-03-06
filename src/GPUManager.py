import py3nvml
from DataManager import GPULog, session
from config.const import MESSAGE_RUN, MESSAGE_STOP, MESSAGE_CHANGE_TEMPLATE, MESSAGE_TEMPLATE
import datetime


def now():
    DIFF_JST_FROM_UTC = 9
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
    return str(now)


class GPUManager:
    def __init__(self):
        self.latest_state = None

    def confirm_current_gpu_state(self):
        free_gpus = py3nvml.get_free_gpus()
        used_gpus = [not state for state in free_gpus]
        state = GPULog()
        state.save_state_list(used_gpus)
        self.latest_state = state

    def _save_state(self):
        session.add(self.latest_state)
        session.commit()

    def generate_message(self, last_state):
        change_message = []
        run_ids = []
        stop_ids = []
        for idx, current_gpu_state in enumerate(self.latest_state.state_list):
            if current_gpu_state:
                run_ids.append(str(idx))
            else:
                stop_ids.append(str(idx))
            if last_state[idx] != current_gpu_state:
                last_state_message = MESSAGE_RUN if last_state[idx] else MESSAGE_STOP
                current_state_message = MESSAGE_RUN if current_gpu_state else MESSAGE_STOP
                diff = str(self.latest_state.created_at - last_state.created_at)
                change_message.append(MESSAGE_CHANGE_TEMPLATE.format(gpu_id=idx,
                                                                     last_state=last_state_message,
                                                                     current_state=current_state_message,
                                                                     diff=diff))
        run_ids = ", ".join(run_ids)
        stop_ids = ", ".join(stop_ids)
        change_message = "".join(change_message)
        message = MESSAGE_TEMPLATE.format(
            time=str(now()),
            run_gpu_ids=run_ids,
            stop_gpu_ids=stop_ids,
            change_message=change_message)
        return message

    def main(self):
        message = ""
        last_state = GPULog.latest_state()
        self.confirm_current_gpu_state()
        print(now())
        if self.latest_state != last_state:
            print(now(), "changed")
            self._save_state()
            message = self.generate_message(last_state)
        return message
