import sqlite3
# import speedtest
import time

def initialize_database():
    """Create SQLite database and table if they do not exist."""
    connection = sqlite3.connect("network_speeds.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS speedtests (
            timestamp INTEGER,
            download_speed REAL,
            upload_speed REAL,
            ping REAL,
            ip_address TEXT,
            other_info TEXT
        )
    ''')
    connection.commit()
    connection.close()

# def perform_speedtest():
#     """Run the speedtest and return the results."""
#     st = speedtest.Speedtest()
#     st.get_best_server()
#     download_speed = st.download() / 1e6  # Convert from bps to Mbps
#     upload_speed = st.upload() / 1e6  # Convert from bps to Mbps
#     ping = st.results.ping
#     ip_address = st.results.client['ip']
#     return (download_speed, upload_speed, ping, ip_address)

def save_results(results):
    """Insert the results into the SQLite database."""
    timestamp = int(time.time())
    download_speed, upload_speed, ping, ip_address = results
    connection = sqlite3.connect("network_speeds.db")
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO speedtests (timestamp, download_speed, upload_speed, ping, ip_address, other_info)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, download_speed, upload_speed, ping, ip_address, ""))
    connection.commit()
    connection.close()

# To prevent the PCI from executing these during development:
# initialize_database()
# results = perform_speedtest()
# save_results(results)