INSERT INTO courses (name, code) VALUES
    ('Computer Science', 'CS101'),
    ('Data Science', 'DS201'),
    ('Software Engineering', 'SE301');

INSERT INTO students (name, email, birth_date) VALUES
    ('Aigerim Nurlanova', 'aigerim.n@example.com', '2007-03-14'),
    ('Dias Serikov', 'dias.s@example.com', '2006-11-02'),
    ('Aruzhan Bekova', 'aruzhan.b@example.com', '2007-07-21'),
    ('Alikhan Omarov', 'alikhan.o@example.com', '2006-05-09'),
    ('Madina Tulegenova', 'madina.t@example.com', '2007-01-30'),
    ('Timur Abenov', 'timur.a@example.com', '2006-09-17'),
    ('Zhanel Mukanova', 'zhanel.m@example.com', '2007-04-25'),
    ('Daniyar Sadykov', 'daniyar.s@example.com', '2006-12-08'),
    ('Amina Ospanova', 'amina.o@example.com', '2007-08-12'),
    ('Yerlan Zhaksylykov', 'yerlan.z@example.com', '2006-02-19');

INSERT INTO enrollments (student_id, course_id, grade) VALUES
    -- CS101
    (1, 1, 92),
    (2, 1, 85),
    (3, 1, 78),
    (4, 1, 85),
    (5, 1, NULL),
    (6, 1, 90),
    -- DS201
    (1, 2, 70),
    (3, 2, 65),
    (7, 2, 74),
    (8, 2, NULL),
    (9, 2, 68),
    -- SE301
    (2, 3, 88),
    (4, 3, 91),
    (5, 3, 95),
    (7, 3, 82),
    (10, 3, 76),
    (9, 3, 91);