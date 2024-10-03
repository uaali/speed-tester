import speedtest
from datetime import datetime

def perform_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping

    return download_speed, upload_speed, ping

def save_speed_test_to_file(file_name='speedtest_results.txt'):
    download_speed, upload_speed, ping = perform_speed_test()
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    result = (
        f"Speed Test Results - {current_time}\n"
        f"Download Speed: {download_speed:.2f} Mbps\n"
        f"Upload Speed: {upload_speed:.2f} Mbps\n"
        f"Ping: {ping:.2f} ms\n"
        "----------------------------------------\n"
    )
    
    with open(file_name, 'a') as f:
        f.write(result)

    print(f"Speed test result saved to {file_name}")

# Run the speed test and save results to a file
save_speed_test_to_file()
