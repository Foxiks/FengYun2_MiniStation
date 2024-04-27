import time, subprocess, signal, psutil, sys
from FengYun2_MiniStation_Parameters_Loader import loader

class FengYun2_MiniStation_Runner:
    def __init__(self) -> None:
        self.state=False
        self.params=loader(settings_file=f'{sys.argv[1]}settings.json')
        self.main()
        pass

    def run_gnuradio_script(self) -> None:
        self.process = subprocess.Popen(['python3', f'{sys.argv[1]}FengYun2_Demodulator.py',
                                         '--driver', self.params.driver,
                                         '--amp', self.params.amp,
                                         '--vga', self.params.vga,
                                         '--lna', self.params.lna,
                                         '--udp-frames-port', self.params.udp_frames_port,
                                         '--rx-freq', self.params.rx_freq,
                                         '--out-path', self.params.out_path,
                                         '--costas-loop-bw', self.params.costas_loop_bw,
                                         '--samp-rate-rx', self.params.samp_rate_rx,
                                         '--threshold', self.params.threshold])
        self.pid = self.process.pid
        return

    def main(self) -> None:
        while True:
            current_minute = int(time.strftime("%M"))
            if current_minute == 58 and self.state == False:
                self.run_gnuradio_script()
                self.state = True
            elif current_minute == 28 and self.state == True:
                psutil.Process(self.pid).send_signal(signal.SIGINT)
                self.state = False
            else:
                time.sleep(10)

if __name__ == "__main__":
    FengYun2_MiniStation_Runner()