def make_scaling_decision(predicted_cpu):
    """
    Make decision based on predicted CPU usage.
    """
    if predicted_cpu > 75:
        return "scale_up"
    elif predicted_cpu < 25:
        return "scale_down"
    else:
        return "no_action"
