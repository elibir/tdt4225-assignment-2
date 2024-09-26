# Define the MySQL table creation queries using a dictionary
TABLES = {}

TABLES['User'] = (
    "CREATE TABLE `User` ("
    "  `id` VARCHAR(255) NOT NULL,"
    "  `has_labels` BOOLEAN NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

TABLES['Activity'] = (
    "CREATE TABLE `Activity` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `user_id` VARCHAR(255) NOT NULL,"
    "  `transportation_mode` VARCHAR(50),"
    "  `start_date_time` DATETIME NOT NULL,"
    "  `end_date_time` DATETIME NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

TABLES['TrackPoint'] = (
    "CREATE TABLE `TrackPoint` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `activity_id` INT NOT NULL,"
    "  `lat` DOUBLE NOT NULL,"
    "  `lon` DOUBLE NOT NULL,"
    "  `altitude` INT,"
    "  `date_days` DOUBLE,"
    "  `date_time` DATETIME NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`activity_id`) REFERENCES `Activity` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)