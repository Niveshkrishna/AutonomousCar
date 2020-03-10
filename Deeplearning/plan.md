project directory:
- Deeplearning
    - model.py (Deeplearning model based on CNN)
    - __init__.py
    - test.py
    - train.py
    - predict.py (Takes an image as input, returns driving parameters)
    - setup.py (Takes care of installing all required files, and establishing connection with control unit mounted on car)
    - main.py
    - collection.py (Data collection of all driving parameters from car unit while manual driving and mapping it with each frame of image and saving it into .csv file )
    - train_data.csv
    - test_data.csv
- Control Unit

# Driving Parameters:
- Steering angle: 
    - variable_name -> steering_angle
    - range -> -30 to +30 degrees with 0 degrees being co-linear with x-axis
    - description -> This angle will be used to drive the stepper motor which controls the steering of car
- Motor speed: 
    - variable_name -> motor_speed 
    - range -> -1 to 1
    - description -> This will be multiplied with a contant value to give the required motor speed. Motors mounted at the rear car will be powering the car based on this value
- Object severity:
    - variable_name -> object_severity
    - range -> 0 to 1
    - description -> Detect objects and classify them based on severity, for Ex: Red signal has 1 severity, green signal has 0 severity, object on lane and signages has some severity. Based on severity, steering_angle and motor_speed will vary
