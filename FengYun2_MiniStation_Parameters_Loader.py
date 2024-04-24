import json

class loader:
    def __init__(self, settings_file) -> None:
        with open(settings_file) as file:
            data=json.load(file)
        print(data)
        self.driver=data['driver']
        self.lna=data['lna']
        self.vga=data['vga']
        self.amp=data['amp']
        self.samp_rate_rx=data['samp_rate_rx']
        self.rx_freq=data['rx_freq']
        self.costas_loop_bw=data['costas_loop_bw']
        self.threshold=data['threshold']
        self.out_path=data['out_path']
        self.udp_frames_port=data['udp_frames_port']
        pass