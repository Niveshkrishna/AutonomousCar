from playsound import playsound
from bluetooth import discover_devices


def main():
    playsound("../song.mp3")
    is_home = False
    print('Press Esc to end....')
    while True:
        print('Performing Enquire')

        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                break

        nearby_devices = discover_devices(lookup_names=True)
        print('found {0} devices'.format(len(nearby_devices)))
        if nearby_devices:
            for address, name in nearby_devices:
                print(' {0} - {1}'.format(address, name))
                if name == 'Joelk':
                    is_home = True
                    break
            else:
                is_home = False

            if is_home:
                if sound.get_num_channels() > 0:
                    print('Playing')
                else:
                    sound.play()
            else:
                sound.stop()
                print('Not Playing')


if __name__ == '__main__':
    main()