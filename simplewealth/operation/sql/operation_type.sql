CREATE TABLE IF NOT EXISTS operation_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR UNIQUE NOT NULL
);

INSERT INTO operation_type(name)
VALUES ('purchase'), ('sale'), ('yield')
ON CONFLICT DO NOTHING;
