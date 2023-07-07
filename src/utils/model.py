#this file will deal with tasks related to model..

import io
import logging

def log_model_summary(model):
    with io.StringIO() as stream:
        model.summary(
            print_fn=lambda x: stream.write(f"{x}\n")
            )
        summary_str = stream.getvalue()
    return summary_str

#this is behaving as io. string format. and updating the model summary in the log file..