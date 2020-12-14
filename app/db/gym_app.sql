DROP TABLE bookings;
DROP TABLE members;
DROP TABLE workouts;

CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    upcoming BOOLEAN,
    date DATE,
    start_time TIME,
    capacity INT,
    booked INT
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(255),
    age INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    workout_id INT REFERENCES workouts(id) ON DELETE CASCADE
);
