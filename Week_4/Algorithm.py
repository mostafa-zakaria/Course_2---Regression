def compute_seconds_block(observations, lambdas, num_blocks):
    num_iterations = lambdas * num_blocks
    return(num_iterations)

def compute_seconds(observations, lambdas, vl_size):
    num_iterations = observations / vl_size
    num_iterations *= lambdas
    return (num_iterations)

def compute_minutes(seconds):
    minutes = seconds / 60
    return(minutes)

def compute_hours(seconds):
    hours = compute_minutes(seconds) / 60
    return(hours)

def compute_days(seconds):
    days = compute_hours(seconds) / 24
    return(days)

def compute_years(seconds):
    years = compute_days(seconds) / 365
    return(years)


observations = 1000000
lambdas = 100
vl_size  = 1
options = [6, 36, 600, 3600]

for v in options:
    print("Total number of Hours for k = "+ str(v) + " is > " + str(compute_hours(compute_seconds_block(observations, lambdas, v))))


#print("Total Number of years> " + str(compute_years(compute_seconds(observations, lambdas, vl_size))))
    
