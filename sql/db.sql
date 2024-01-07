CREATE TABLE IF NOT EXISTS personal_info(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS fiscal_info(
    rfc VARCHAR(13) PRIMARY KEY,
    personal_id INTEGER,
    FOREIGN KEY(personal_id) references personal_info(id)
);

CREATE TABLE IF NOT EXISTS query_log(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    query_date DATETIME,
    request_parameters VARCHAR(255),
    result VARCHAR(255)
);