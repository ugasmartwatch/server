CREATE TABLE IF NOT EXISTS profiles (
	device_id TEXT NOT NULL,
	config TEXT NOT NULL,
	create_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS syncs (
	device_id TEXT NOT NULL,
	data TEXT NOT NULL,
	create_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX profiles_device_id_index ON profiles(device_id);

CREATE INDEX syncs_device_id_index ON syncs(device_id);
