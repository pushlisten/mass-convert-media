import os, shutil, subprocess, time, psutil

if os.path.exists('C:\\scripts\\convert.lock'):
    exit()
else:
    open('C:\\scripts\\convert.lock', 'a').close()

source = "D:\\Media\\Sonarr"
target = "D:\\Media\\Shows-480p"
ffmpegFlags = "-c:v libx265 -vtag hvc1 -vf scale=720:480 -crf 28 -preset veryslow " + "-c:a libopus -b:a 96K " + "-map_chapters -1 -dn -sn -metadata title=\"\" -fflags +bitexact -flags:v +bitexact -flags:a +bitexact"
supportedFormats = ['mkv', 'mp4', 'mov', '3dostr', '3g2', '3gp', '4xm', 'a64', 'aa', 'aac', 'aax', 'ac3', 'ace', 'acm', 'act', 'adf', 'adp', 'ads', 'adts', 'adx', 'aea', 'afc', 'aiff', 'aix', 'alaw', 'alias_pix', 'alp', 'amr', 'amrnb', 'amrwb', 'amv', 'anm', 'apac', 'apc', 'ape', 'apm', 'apng', 'aptx', 'aptx_hd', 'aqtitle', 'argo_asf', 'argo_brp', 'argo_cvg', 'asf', 'asf_o', 'asf_stream', 'ass', 'ast', 'au', 'av1', 'avi', 'avif', 'avisynth', 'avm2', 'avr', 'avs', 'avs2', 'avs3', 'bethsoftvid', 'bfi', 'bfstm', 'bin', 'bink', 'binka', 'bit', 'bitpacked', 'bmp_pipe', 'bmv', 'boa', 'bonk', 'brender_pix', 'brstm', 'c93', 'caf', 'cavsvideo', 'cdg', 'cdxl', 'chromaprint', 'cine', 'codec2', 'codec2raw', 'concat', 'crc', 'cri_pipe', 'dash', 'data', 'daud', 'dcstr', 'dds_pipe', 'derf', 'dfa', 'dfpwm', 'dhav', 'dirac', 'dnxhd', 'dpx_pipe', 'dsf', 'dshow', 'dsicin', 'dss', 'dts', 'dtshd', 'dv', 'dvbsub', 'dvbtxt', 'dvd', 'dxa', 'ea', 'ea_cdata', 'eac3', 'epaf', 'exr_pipe', 'f32be', 'f32le', 'f4v', 'f64be', 'f64le', 'ffmetadata', 'fifo', 'fifo_test', 'film_cpk', 'filmstrip', 'fits', 'flac', 'flic', 'flv', 'framecrc', 'framehash', 'framemd5', 'frm', 'fsb', 'fwse', 'g722', 'g723_1', 'g726', 'g726le', 'g729', 'gdigrab', 'gdv', 'gem_pipe', 'genh', 'gif', 'gif_pipe', 'gsm', 'gxf', 'h261', 'h263', 'h264', 'hash', 'hca', 'hcom', 'hdr_pipe', 'hds', 'hevc', 'hls', 'hnm', 'ico', 'idcin', 'idf', 'iff', 'ifv', 'ilbc', 'image2', 'image2pipe', 'imf', 'ingenient', 'ipmovie', 'ipod', 'ipu', 'ircam', 'ismv', 'iss', 'iv8', 'ivf', 'ivr', 'j2k_pipe', 'jacosub', 'jpeg_pipe', 'jpegls_pipe', 'jpegxl_pipe', 'jv', 'kux', 'kvag', 'laf', 'latm', 'lavfi', 'libgme', 'libopenmpt', 'live_flv', 'lmlm4', 'loas', 'lrc', 'luodat', 'lvf', 'lxf', 'm4v', 'matroska', 'matroska,webm', 'mca', 'mcc', 'md5', 'mgsts', 'microdvd', 'mjpeg', 'mjpeg_2000', 'mkvtimestamp_v2', 'mlp', 'mlv', 'mm', 'mmf', 'mods', 'moflex', 'mov', 'mov,mp4,m4a,3gp,3g2,mj2', 'mp2', 'mp3', 'mp4', 'mpc', 'mpc8', 'mpeg', 'mpeg1video', 'mpeg2video', 'mpegts', 'mpegtsraw', 'mpegvideo', 'mpjpeg', 'mpl2', 'mpsub', 'msf', 'msnwctcp', 'msp', 'mtaf', 'mtv', 'mulaw', 'musx', 'mv', 'mvi', 'mxf', 'mxf_d10', 'mxf_opatom', 'mxg', 'nc', 'nistsphere', 'nsp', 'nsv', 'null', 'nut', 'nuv', 'obu', 'oga', 'ogg', 'ogv', 'oma', 'openal', 'opus', 'paf', 'pam_pipe', 'pbm_pipe', 'pcx_pipe', 'pfm_pipe', 'pgm_pipe', 'pgmyuv_pipe', 'pgx_pipe', 'phm_pipe', 'photocd_pipe', 'pictor_pipe', 'pjs', 'pmp', 'png_pipe', 'pp_bnk', 'ppm_pipe', 'psd_pipe', 'psp', 'psxstr', 'pva', 'pvf', 'qcp', 'qdraw_pipe', 'qoi_pipe', 'r3d', 'rawvideo', 'realtext', 'redspark', 'rka', 'rl2', 'rm', 'roq', 'rpl', 'rsd', 'rso', 'rtp', 'rtp_mpegts', 'rtsp', 's16be', 's16le', 's24be', 's24le', 's32be', 's32le', 's337m', 's8', 'sami', 'sap', 'sbc', 'sbg', 'scc', 'scd', 'sdl,sdl2', 'sdns', 'sdp', 'sdr2', 'sds', 'sdx', 'segment', 'ser', 'sga', 'sgi_pipe', 'shn', 'siff', 'simbiosis_imx', 'sln', 'smjpeg', 'smk', 'smoothstreaming', 'smush', 'sol', 'sox', 'spdif', 'spx', 'srt', 'stl', 'stream_segment,ssegment', 'streamhash', 'subviewer', 'subviewer1', 'sunrast_pipe', 'sup', 'svag', 'svcd', 'svg_pipe', 'svs', 'swf', 'tak', 'tedcaptions', 'tee', 'thp', 'tiertexseq', 'tiff_pipe', 'tmv', 'truehd', 'tta', 'ttml', 'tty', 'txd', 'ty', 'u16be', 'u16le', 'u24be', 'u24le', 'u32be', 'u32le', 'u8', 'uncodedframecrc', 'v210', 'v210x', 'vag', 'vbn_pipe', 'vc1', 'vc1test', 'vcd', 'vfwcap', 'vidc', 'vividas', 'vivo', 'vmd', 'vob', 'vobsub', 'voc', 'vpk', 'vplayer', 'vqf', 'w64', 'wady', 'wav', 'wavarc', 'wc3movie', 'webm', 'webm_chunk', 'webm_dash_manifest', 'webp', 'webp_pipe', 'webvtt', 'wsaud', 'wsd', 'wsvqa', 'wtv', 'wv', 'wve', 'xa', 'xbin', 'xbm_pipe', 'xmd', 'xmv', 'xpm_pipe', 'xvag', 'xwd_pipe', 'xwma', 'yop', 'yuv4mpegpipe']

ffmpegCount = 0

for subdir, dirs, files in os.walk(source):
    if not os.path.isdir(subdir.replace(source, target)):
        os.mkdir(subdir.replace(source, target))

    for file in files:
        if os.path.exists(subdir.replace(source, target) + '\\' + file) or os.path.exists(subdir.replace(source, target) + '\\' + file.split('.')[0] + '.mkv'):
            continue
        
        if file.split('.')[-1] in supportedFormats:
            print(file)
            with open("C:\\scripts\\convert.log", "a") as log:
                log.write(file + '\n')

            subprocess.Popen('ffmpeg -i \"' + subdir + '\\' + file + '\" ' + ffmpegFlags + ' \"' + subdir.replace(source, target) + '\\' + file.split('.')[0] + '.mkv\"', shell=True)
            ffmpegCount += 1

            while ffmpegCount >= 3:
                time.sleep(5)
                processlist=list()
                for process in psutil.process_iter():
                    if process.name() == 'ffmpeg.exe':
                        processlist.append(process.name())
                ffmpegCount = len(processlist)
        else:
            shutil.copyfile(subdir + '\\' + file, subdir.replace(source, target) + '\\' + file)

os.remove('C:\\scripts\\convert.lock')
