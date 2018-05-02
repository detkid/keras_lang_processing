from chardet.universaldetector import UniversalDetector

def check_encoding(file_path):
    detector = UniversalDetector()
    with open(file_path, mode='rb') as f:
        for binary in f:
            detector.feed(binary)
            if detector.done:
                break
    detector.close()
    print(detector.result, end='')
    print(detector.result['encoding'], end='')

def main():
    check_encoding('nogizaka_lyric_test.txt')

if __name__ == '__main__':
    main()