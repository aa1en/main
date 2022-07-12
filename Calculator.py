def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    try:
        print("Ընտրեք գործողությունը. \n1)Գումարել \n2)Հանել \n3)Բազմապատկել \n4)Բաժանել")
        choice = input("Մուտքագրեք թվանշանը(1,2,3,4): ")
        if choice in ('1', '2', '3', '4'):
            try:
                if choice == '1':
                    try:
                        num1 = float(input("Մուտքագրեք առաջին թիվը․ > "))
                        num2 = float(input("Մուտքագրեք երկրորդ թիվը․ > "))
                        print(f'{num1} + {num2} = {add(num1, num2)}')
                    except ValueError:
                        print('Մուտքագրեք թվեր։')
                        continue
                    except KeyboardInterrupt:
                        print('Մուտքագրեք միայն արժեքներ!!!!')
                        continue
                if choice == '2':
                    try:
                        num1 = float(input("Մուտքագրեք առաջին թիվը․ > "))
                        num2 = float(input("Մուտքագրեք երկրորդ թիվը․ > "))
                        print(f'{num1} - {num2} = {subtract(num1, num2)}')
                    except ValueError:
                        print('Մուտքագրեք թվեր։')
                        continue
                    except KeyboardInterrupt:
                        print('Մուտքագրեք միայն արժեքներ!!!!')
                        continue
                if choice == '3':
                    try:
                        num1 = float(input("Մուտքագրեք առաջին թիվը․ > "))
                        num2 = float(input("Մուտքագրեք երկրորդ թիվը․ > "))
                        print(f'{num1} * {num2} = {multiply(num1, num2)}')
                    except ValueError:
                        print('Մուտքագրեք թվեր։')
                        continue
                    except KeyboardInterrupt:
                        print('Մուտքագրեք միայն արժեքներ!!!!')
                        continue
                if choice == '4':
                    try:
                        num1 = float(input("Մուտքագրեք առաջին թիվը․ > "))
                        num2 = float(input("Մուտքագրեք երկրորդ թիվը․ > "))
                        print(f'{num1} / {num2} = {divide(num1, num2)}')
                    except ValueError:
                        print('Մուտքագրեք թվեր։ ')
                        continue
                    except KeyboardInterrupt:
                        print('Մուտքագրեք միայն արժեքներ!!!!')
                        continue
                    except ZeroDivisionError:
                        print('Թիվը չի կարելի բաժանել 0-ի վրա։ ')
            except KeyboardInterrupt:
                print('Yntreq nshvac tarberakneric.')
            next_calculation = input("Կատարե՞լ հաջորդ հաշվարկը (այո/ոչ): ").lower()
            if next_calculation == "ոչ":
                break
    except KeyboardInterrupt:
        print('Ընտրեք գործողություններից ինչ-որ մեկը։')


