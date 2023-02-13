from scraping.rng_scrapper import RNGScrapper
from Cryptodome.Random import random
import scraping.constants as const
from time import sleep


class Main:
    
    def run_scrapper(self):
        
        # Could be inputs
        all_numbers = list()
        min = pow(10, 11)
        max = pow(10, 12) - 1
        total = 10000000

        try:
            with RNGScrapper(const.DRIVERS_DIR) as bot:
                
                print('Initializing...\n')

                while len(all_numbers) < total:
                    
                    # Sets the fields and then submit to generate
                    bot.initiate_browser()
                    bot.set_min_number(min)
                    bot.set_max_number(max)

                    # Amount of numbers to be generated is defined randomly on each request (website limit -> 1000), again to avoid IP block
                    n = random.randint(800, 1000)
                    bot.set_how_many(n)
                    bot.submit_information()

                    # Export each numbers batch to a file, as far as they're being generated 
                    str_numbers = bot.extract_generated_numbers()
                    with open('output.txt', 'a') as file:
                        file.write('\n')
                        file.write(str_numbers)

                    # Handles the generated numbers and add them to the list
                    n_list = str_numbers.split(', ')
                    numbers = list(map(int, n_list))
                    all_numbers += numbers

                    # Monitoring scraping progress
                    progress = (len(all_numbers) / total) * 100.0
                    print(f'{round(progress, 2)}% concluded...')

                    # Waiting time defined randomly between each request to avoid IP block
                    timing = random.randint(2, 4)
                    sleep(timing)
                
                print('\nFinalized!\n')

        except Exception as excp:

            if 'in PATH' in str(excp):
                print(
                    'If you are trying to run the bot from command line\n'
                    'Please add to PATH (environment variables) your Selenium Drivers\n\n'
                    'Windows --> set PATH=%PATH%;C:path-to-your-folder\n\n'
                    'Linux   --> PATH=$PATH:/path/toyour/folder/\n'
                )
            else:
                raise

        # Result
        size = len(all_numbers)
        uniques = len(set(all_numbers))
        print(f'{size - uniques} repeats in {size} generated numbers!')


if __name__ == '__main__':
    Main().run_scrapper()
    