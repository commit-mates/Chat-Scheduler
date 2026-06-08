--for Contacts Table

CREATE TABLE IF NOT EXISTS contacts ( 
    contact_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

 -- for  Scheduled Messages Table

CREATE TABLE IF NOT EXISTS scheduled_messages (
    message_id SERIAL PRIMARY KEY,
    contact_id INTEGER NOT NULL,
    message_content TEXT NOT NULL,
    scheduled_time TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'unsent',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sent_at TIMESTAMP,

    CONSTRAINT fk_contact
        FOREIGN KEY(contact_id)
        REFERENCES contacts(contact_id)
        ON DELETE CASCADE
);

--for  Notification Logs Table

CREATE TABLE IF NOT EXISTS notification_logs (
    notification_id SERIAL PRIMARY KEY,
    message_id INTEGER NOT NULL,
    notification_text TEXT,
    notification_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_message
        FOREIGN KEY(message_id)
        REFERENCES scheduled_messages(message_id)
        ON DELETE CASCADE
);

-- for  Scheduler Logs Table

CREATE TABLE IF NOT EXISTS scheduler_logs (log_id SERIAL PRIMARY KEY,action VARCHAR(100),
    status VARCHAR(20),
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT
);
