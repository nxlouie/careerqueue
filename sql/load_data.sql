# load_data.sql

INSERT INTO Recruiter (recruiter_id, firstname, lastname, total_time_sum, total_talks, last_start) VALUES
  (NULL, 'John', 'Doe', 0, 0, CURRENT_TIMESTAMP),
  (NULL, 'Bob', 'Brick', 0, 0, CURRENT_TIMESTAMP),
  (NULL, 'Tim', 'Bolt', 0, 0, CURRENT_TIMESTAMP);

INSERT INTO Ticket (ticket_num, firstname, lastname, phone, email, major, grad_year, recruiter_id) VALUES
  (NULL, 'Justin', 'Parus', '4087028940', 'jp@esnail.com', 'CS', '2018', NULL),
  (NULL, 'Diego', 'Holt', '4087028940', 'dh@mom.com', 'CS', '2017', NULL),
  (NULL, 'Nathan', 'Louie', '5862911318', 'nl@help.com', 'CS', '2018', NULL);

INSERT INTO Metrics (metric_id, metric_name) VALUES
  (NULL, 'C++'),
  (NULL, 'Python'),
  (NULL, 'HTML'),
  (NULL, 'Ruby'),
  (NULL, 'Swift');

INSERT INTO StudentMetrics (ticket_num, metric_id, proficiency) VALUES
(1, 1, 5),
(1, 2, 3),
(1, 3, 3),
(1, 4, 1),
(1, 5, 4),
(2, 1, 5),
(2, 2, 4),
(2, 3, 4),
(2, 4, 1),
(2, 5, 1),
(3, 1, 5),
(3, 2, 4),
(3, 3, 4),
(3, 4, 2),
(3, 5, 1);
