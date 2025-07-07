def execute_scaling(decision):
    """
    Simulate scaling action.
    """
    if decision == "scale_up":
        print("Scaling up resources...")
    elif decision == "scale_down":
        print("Scaling down resources...")
    else:
        print("No scaling action needed.")
