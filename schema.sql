DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
CREATE TABLE courses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(10) NOT NULL UNIQUE
);
CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    birth_date DATE CHECK (birth_date < CURRENT_DATE) ,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE enrollments(
    id SERIAL PRIMARY KEY,
    student_id INT NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    course_id INT NOT NULL REFERENCES courses(id) ON DELETE RESTRICT,
    grade INT CHECK (grade >= 0 AND grade <= 100),
    enrollment_date TIMESTAMP DEFAULT NOW(),
    UNIQUE(student_id, course_id)
);
INSERT INTO students (name, email) VALUES ('Test', 'test@example.com');
INSERT INTO courses (name, code) VALUES ('Intro to CS', 'CS101');
INSERT INTO enrollments (student_id, course_id) VALUES (1, 1);
INSERT INTO enrollments (student_id, course_id) VALUES (1, 1);
