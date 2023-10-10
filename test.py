import punishment

if __name__ == '__main__':
    print(punishment.do_punishment('Je ne jetterai plus de cacahuètes', 'sur le professeur.', 3))
    print(punishment.do_punishment('Je ne jetterai plus de cacahuètes', 'sur le professeur.        ', 3))
    print(punishment.do_punishment('Je ne jetterai plus de cacahuètes', '   sur le professeur', 3))