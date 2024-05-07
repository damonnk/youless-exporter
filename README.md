# Youless-Exporter
What is a youless? See: https://www.youless.nl/watis.html

The code available in this repo can be used to create a docker image and run it as a container to collect data from a youless meter with Prometheus.
This code was tested with a youless LS110 and firmware version 1.2.0


Clone the repo and build the image
```
git clone https://github.com/damonnk/youless-exporter.git
cd youless-exporter/ 
docker build -t youless-exporter .
```

When the image is build you can start the container with a docker run command
```
docker run -d -p 9101:9101 \
	 --name youless_exporter \
	 --restart unless-stopped \
	 -e youless=x.x.x.x \
	 youless-exporter
```

Replace the x.x.x.x with the IP address or hostname of your youless.
The script inside the container is listening on port 9101.
If that port is already in use you can change the port docker listens on by change the first number, for example: 8989:9101
When the container is running you can test if it is working
```
$ curl http://localhost:9101
# HELP youless_current_power_usage Current Power Usage in Watts
# TYPE youless_current_power_usage gauge
youless_current_power_usage 288.0
# HELP youless_total_power_usage Total Power Usage in kWh
# TYPE youless_total_power_usage gauge
youless_total_power_usage 10028.558

```

You can use the folling config for Prometheus
```
  - job_name: 'youless'
    static_configs:
     - targets: [ 'x.x.x.x:9101' ]
```
Replace the x.x.x.x with the IP address of your dockerhost

