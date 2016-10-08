# Create Tables

CREATE TABLE Recruiter (
  recruiter_id    int           NOT NULL AUTO_INCREMENT,
  firstname       varchar(20)   NOT NULL,
  lastname        varchar(20)   NOT NULL,
  total_time_sum  double        NOT NULL,
  total_talks     int           NOT NULL,
  last_start      TIMESTAMP     NOT NULL,
  PRIMARY KEY (recruiter_id)
);

CREATE TABLE Ticket (
  ticket_num      int           NOT NULL AUTO_INCREMENT,
  firstname       varchar(20)   NOT NULL,
  lastname        varchar(20)   NOT NULL,
  phone           varchar(20)   NOT NULL,
  email           varchar(40)   NOT NULL,
  major           varchar(5)    NOT NULL,
  grad_year       varchar(4)    NOT NULL,
  done            bit           NOT NULL,
  recruiter_id    int           NOT NULL,
  PRIMARY KEY (ticket_num),
  FOREIGN KEY (recruiter_id)    REFERENCES Recruiter (recruiter_id)
);

CREATE TABLE Metrics (
  metric_id       int           NOT NULL AUTO_INCREMENT,
  metric_name     varchar(20)   NOT NULL,
  PRIMARY KEY (metric_id)
);

CREATE TABLE StudentMetrics (
  ticket_num      int           NOT NULL,
  metric_id       int           NOT NULL,
  proficiency     int           NOT NULL,
  PRIMARY KEY (metric_id),
  FOREIGN KEY (metric_id)       REFERENCES Ticket  (ticket_num),
  FOREIGN KEY (ticket_num)      REFERENCES Metrics (metric_id)
);
