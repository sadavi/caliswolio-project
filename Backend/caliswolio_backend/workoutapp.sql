-- Table for exercises
CREATE TABLE Exercise(
    Exercise_ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Category TEXT NOT NULL,
    Level TEXT NOT NULL,
    Description TEXT
);

-- Table for member account
CREATE TABLE Member_account(
    Member_ID INTEGER PRIMARY KEY,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    Phone_Number TEXT NOT NULL,
    Level_ID INTEGER NOT NULL,
    Birth_Year INTEGER NOT NULL,
    Gender TEXT NOT NULL,
    Zipcode INTEGER NOT NULL
);

-- Table for exercise template exercises
CREATE TABLE Template_Exercises(
    Template_Ex_ID INTEGER PRIMARY KEY,
    Template_ID INTEGER NOT NULL,
    Exercise_ID INTEGER NOT NULL,
    Target_Sets INTEGER,
    Target_Reps INTEGER,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Template_ID) REFERENCES Template_Workout(Template_ID)
);

-- Table for prior workout exercises
CREATE TABLE Prior_Workout_Exercises(
    Prior_Workout_Ex_ID INTEGER PRIMARY KEY,
    Exercise_ID INTEGER NOT NULL,
    Workout_ID INTEGER NOT NULL,
    Target_Sets INTEGER,
    Target_Reps INTEGER,
    Actual_Sets INTEGER,
    Actual_Reps INTEGER,
    Position_In_List INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Workout_ID) REFERENCES Prior_Workout(Workout_ID)
);

-- Table for future workout exercises
CREATE TABLE Future_Workout_Exercises(
    Future_Workout_Ex_ID INTEGER PRIMARY KEY,
    Future_Workout_ID INTEGER NOT NULL,
    Exercise_ID INTEGER NOT NULL,
    Target_Sets INTEGER,
    Target_Reps INTEGER,
    Position_In_List INTEGER NOT NULL,
    FOREIGN KEY (Exercise_ID) REFERENCES Exercise(Exercise_ID),
    FOREIGN KEY (Future_Workout_ID) REFERENCES Future_Workout(Future_Workout_ID)
);

-- Table for workout templates
CREATE TABLE Template_Workout(
    Template_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID INTEGER NOT NULL,
    Name TEXT NOT NULL,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

-- Table for prior workouts
CREATE TABLE Prior_Workout(
    Workout_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID INTEGER NOT NULL,
    When_Completed DATE,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

-- Table for holding future workouts
CREATE TABLE Future_Workout(
    Future_Workout_ID INTEGER PRIMARY KEY,
    Member_ID INTEGER NOT NULL,
    Level_ID INTEGER NOT NULL,
    Category_ID INTEGER NOT NULL,
    Name TEXT NOT NULL,
    Perform_On DATE,
    FOREIGN KEY (Level_ID) REFERENCES Member_Account(Level_ID),
    FOREIGN KEY (Member_ID) REFERENCES Member_Account(Member_ID)
);

---- ******************************************************************** ----

INSERT INTO Exercise (Exercise_ID, Name, Category, Level)
VALUES
(1, "Scapular Pull", "Pull-up", "Beginner"),
(2, "Arch hang", "Pull-up", "Beginner"),
(3, "Negative Pull-up", "Pull-up", "Beginner"),
(4, "Pull-up", "Pull-up", "Intermediate"),
(5, "Wide Grip Pull-up", "Pull-up", "Intermediate"),
(6, "L-sit Pull-up", "Pull-up", "Advanced"),
(7, "Muscle-up", "Pull-up", "Advanced"),
(8, "Vertical Push-up", "Push-up", "Advanced"),
(9, "Incline Push-up", "Push-up", "Beginner"),
(10, "Push-up", "Push-up", "Beginner"),
(11, "Decline Push-up", "Push-up", "Beginner"),
(12, "Diamond Push-up", "Push-up", "Intermediate"),
(13, "Pike Push-up", "Push-up", "Intermediate"),
(14, "Wall Assisted Handstand Push-up", "Push-up", "Intermediate"),
(15, "Pseudo-planche Push-up", "Push-up", "Intermediate"),
(16, "Freestanding Handstand Push-up", "Push-up", "Advanced"),
(17, "Decline Pseudo-planche Push-up", "Push-up", "Advanced"),
(18, "Planche Push-up", "Push-up", "Advanced"),
(19, "Magic Push-up", "Push-up", "Advanced"),
(20, "Static Dip Support Hold", "Dip", "Beginner"),
(21, "Negative Dip", "Dip", "Beginner"),
(22, "Seated Dip", "Dip", "Beginner"),
(23, "Parallel Bar Dip", "Dip", "Intermediate"),
(24, "Straight Bar Dip", "Dip", "Intermediate"),
(25, "Impossible Dip", "Dip", "Advanced"),
(26, "Vertical Row", "Row", "Beginner"),
(27, "Incline Row", "Row", "Beginner"),
(28, "Horizontal Row", "Row", "Intermediate"),
(29, "Wide-grip Incline Row", "Row", "Intermediate"),
(30, "Wide-grip Horizontal Row", "Row", "Advanced"),
(31, "Decline Row", "Row", "Advanced"),
(32, "Assisted Squat", "Squat", "Beginner"),
(33, "Air Squat", "Squat", "Beginner"),
(34, "Bulgarian Split Squat", "Squat", "Beginner"),
(35, "Beginner Shrimp Squat", "Squat", "Intermediate"),
(36, "Intermediate Shrimp Squat", "Squat", "Intermediate"),
(37, "Assisted Pistol Squat", "Squat", "Intermediate"),
(38, "Advanced Shrimp Squat", "Squat", "Advanced"),
(39, "Pistol Squat", "Squat", "Advanced"),
(40, "Dragon Pistol Squat", "Squat", "Advanced"),
(41, "Romanian Deadlift", "Hinge", "Beginner"),
(42, "Single Leg Deadlift", "Hinge", "Intermediate"),
(43, "Banded Nordic Curl Negative", "Hinge", "Intermediate"),
(44, "Banded Nordic Curl", "Hinge", "Advanced"),
(45, "Nordic Curl", "Hinge", "Advanced"),
(46, "Full Plank", "Core", "Beginner"),
(47, "Half Plank", "Core", "Beginner"),
(48, "L-sit", "Core", "Beginner"),
(49, "Hanging Knee-raise", "Core", "Beginner"),
(50, "Sit-up", "Core", "Beginner"),
(51, "Crunch", "Core", "Beginner"),
(52, "Toe-touch", "Core", "Beginner"),
(53, "Superman Hold", "Core", "Beginner"),
(54, "Mountain Climber", "Core", "Beginner"),
(55, "Plank Row", "Core", "Intermediate"),
(56, "Pseudo-planche Hold", "Core", "Intermediate"),
(57, "Crow Hold", "Core", "Intermediate"),
(58, "Leg Raise", "Core", "Intermediate"),
(59, "Bicycle", "Core", "Intermediate"),
(60, "Side Plank With Rotation", "Core", "Intermediate"),
(61, "Banana Roll", "Core", "Intermediate"),
(62, "Hanging L-sit", "Core", "Intermediate"),
(63, "Hanging Leg Raise", "Core", "Intermediate"),
(64, "Reverse Deadlift", "Core", "Advanced"),
(65, "Dragon Flag", "Core", "Advanced"),
(66, "Front Lever", "Core", "Advanced"),
(67, "Single-leg Straight Arm Side Plank", "Core", "Advanced"),
(68, "Planche Hold", "Core", "Advanced");