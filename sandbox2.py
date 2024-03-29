
Text = "TGCCTAAGCATTTTTCTTTTGACCATTGCCTAAGCATTTTTCTTTGCCTAAGCTTGACCATTGCCTAAGCTTGACCATGCAGTTTTTGACCATGCAGTTTTTGACCATTGCCTAAGCATTTTTCTTGCAGTTTCGAAAGTAGGCAGTTTTGCCTAAGCTTGACCATTGCCTAAGCGCAGTTTATTTTTCTTTGCCTAAGCCGAAAGTAGATTTTTCTTTTGACCATTGCCTAAGCCGAAAGTAGATTTTTCTTTTGACCATCGAAAGTAGGCAGTTTGCAGTTTATTTTTCTTATTTTTCTTTGCCTAAGCTTGACCATGCAGTTTGCAGTTTTTGACCATTGCCTAAGCCGAAAGTAGGCAGTTTCGAAAGTAGATTTTTCTTGCAGTTTATTTTTCTTCGAAAGTAGTGCCTAAGCGCAGTTTTTGACCATTTGACCATATTTTTCTTTTGACCATATTTTTCTTATTTTTCTTGCAGTTTTGCCTAAGCTGCCTAAGCTGCCTAAGCTTGACCATTTGACCATGCAGTTTGCAGTTTCGAAAGTAGCGAAAGTAGATTTTTCTTCGAAAGTAGTGCCTAAGCGCAGTTTTTGACCATGCAGTTTCGAAAGTAGTTGACCATTTGACCATTTGACCATTGCCTAAGCTGCCTAAGCCGAAAGTAGTGCCTAAGCCGAAAGTAGCGAAAGTAGCGAAAGTAGTGCCTAAGCTTGACCATTTGACCATTGCCTAAGCTGCCTAAGCCGAAAGTAGGCAGTTTGCAGTTTTGCCTAAGCCGAAAGTAGCGAAAGTAGGCAGTTTCGAAAGTAGTGCCTAAGCCGAAAGTAGTTGACCATTGCCTAAGC"
k = 14

def FrequentWords(Text, k):
    FrequentPatterns = [] # output variable
    # your code here
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

def remove_duplicates(Text):
    ItemsNoDuplicates = []
    for item in Text:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates

def CountDict(Text, k):
    Count = {} # output variable
    # your code here
    for i in range((len(Text))-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

print('FrequentWords')
print(FrequentWords(Text, k))

def inversComplement(input):
    output = ''
    for letter in input:
        letter = letter.upper()

        if letter == 'A':
            output += 'T'
        elif letter == 'T':
            output += 'A'
        elif letter == 'G':
            output += 'C'
        else:
            output += 'G'

    return(output[::-1])

input = "TTATCTGGGGAACTCTTGTCTCTCAAAGCGATAATCATCGCCTATCGGGCAGGAATCTGTGTGGGGCCAATTATGCCAACGAGTTAGTAACTCTAAATAGCTCCCCACCCTTTTACGATTGAGGCTTACACCGGCCATCGGTGGGTAAGTTAGATCACTGGCCGCCTGCCAATCCGAGCGTCCCCTATTAGCTGCAAGGGCACGTCAACAACATCGGCGCGCATTATTGGGCCTTTATCCTGCAGTCCTGGCTGTGTAAGAACTTTCCTCCCGTCACTTATCCCTTATTATGCTACTGGCGCGGTTAGTGTTAAGCGCGCTCCTGGTTTTATATAAGGGGGGGGTGGGACTCTTCATTGGACGCTGGCTCCCGATCTCGGTCCCGCTAGAACGTCAGGAGACGAGGCCGCGAGGCGCGCCTCAAGTCAGAGGCTTACGTTTTACGATCCCTTGGGTCTCGCTGTCGTCCATTGCCGAGGTTGAATGCTGGATTCATGGGTTAAACCATGAGGAGCGTCATATAGTCGGGCTGGAAATATAATGTTTTGAACGTTAAACTCTGCTCTACCTTCCCAGGGAATATCCATCCAGGTTACGCATTATGCAGGCTCCTTCGCCGATCACGCGACCACAGCACCTGAAAGCGGATTGTCTTAGAAACAGCGACTATTTGCACTAACCTAGCGCGCACCCGATCACTCAAACGCGAACGTATGACGACTTGGCCTGTGCCCGGCGCAGGCTAGGAGCAAAGCGCTTACAACCCGCTGCTACGAATTTATGATCAATTATGTGCGAGCAATGAAGGAGGATTTTTCTTAAATAAGTGCAAGCTATCGATCAGAAAGGGTACCGTCTACCAGCGCTAATTCTCAAGCGCAGGTGGACTACAATCCTATGAACTCCACTTGCGACGACAGTTGGCCTCACTTTGGAAAGTAGATACGAACGTAGCTGAGCCGAGCACGTCATAATGGCATCTTTCTGGGATTAAAGTCCACCATCATTATGGTCCGACTTACACGCCTGGCTAACCCACCCCCTCGCCTCCTACAGCTTTGGAGAGAGACAGTCCGACGCTGTTCGGAACAGAAGAGCCGTCGACCCAGGGTCCCCGGTGCGTTCTCCTGTGTCCGGCCCTACAGACGGTAATGGATCGTCCCGTAAGTAAGACGTGAAGATAGCGTCCTGCATATAGATCGTAACTCAATCGAAGTAGGCGCGAAGCAAGGCTCGGGCCCCTTACAGAGCCAGATGGCTTGGCGCCCACGAAGAGACACCCTACAAGAGCCTGCTTTCCGAAGGTCCAACCAGAAGACCGATGCGGAAGCTAGGAGACCTCGGTAGAGATTCCGCCGGAGGGCAGTAGAACTGCGCGGGCGCATCAGGATGACCCTCGGCGGACACGAGATTCAGGTCACTCTGTGTTTGTCGTGTGTATCCGAAGAGATAACGCATTATACACCCTCTGAGCTTGGGCAATTGCGATGCCGTACGTGATTCGTTGGCCCTCTTTTGCCGGGTCTCGAAAGGCTGGAAACTTCTCTAGTTCTATAGGCACCTCACTAGGAGTACAAGAGCCATAAGCCCACACGGCCCAATTGTGCTTGTCGCCGCAGATATCATTTGTGATCACACTCCCCCCCCAAAGGTCGGGCTAAGGCATAGGGCATGAGACCCGTCGATGGTCAGGCGCACGGTATCGAGGCCGACTTAGTGTAAGGCGCGATTCCCAGACGCCTTCGGCGAAATATAGCTGCATCCGGGTACCGCCGCAGCGACAACCTCAGCAGGTGAAGATCAACGCGGGCTAATCGTTCAGTTGAGAACGCCTCGCGAATTCCGGCTTTCTTCGATCACGCCTTGCTGGAAGGATGGTTTCCCGCTCTTACACGATCGTGTTGTCTTTCGGGATAGTAGTCAGGCAACGATACACAGCATCTCAGAACTAGTCTGCGATTGTCCAATTAAGACCTATCAAAAGTTAGCAATAGGAGACCGCAAATCCAGATGCCTGTCGGCACCGTTATAATAACCGGAGGCGTCTTGATGCTGACGACCGTTGGGTTCTTTAGGCATATCAACAGAGGGGGGGCGAATTTGCTGCCTAGCTAACTAATAGGTCATCTGATCTTTGGAGCCTATCAAAGCTTTAGGTGGGCGGCTAACAATAAACTGCCGAGACGGACCCGACGTTGCGATTGTGCCAGTTGTAGGATCGAGAGTTTTCGGAGCAGCTTCTTCCGACGAAGCTACGCTAGCACAGTCCGTTGTGGTTTACAATAGATAGCTTTAATTCACCGAAAGAGTCCTTCTGACCTCTCTCCAGCTCCCAGAACACGGAAGAATGCCAGCGAAGTTGGCTGATGGGGGGGTATTGCGTGCATTCCTCTTTTACACAAGTGGCAGTGGTGCTAGCACTAGACTTCGGGGAGGCCCAATTCACGTTATCCGTAGGGTATCAAGACGCTGTATATTTACTGGGTAAGTGGTGATGTTATGGCCAAGTCAAGCCCTAATATGTGCTTTAGGGTCGGAGATTGGAAACGGAGCAGCGATCAACAGAACTTCTTTCTGGATACTTAGCGAACCTTCTGTGCCGAAGATACGGGACACGTAAGCCCAATGATCAGCATGGCGGTCCAGATTGAAGGGAGTAGGCAACGGAAGTTAACCGCGACCCGGTAGCTGCAGGAGTGGAAGTATATTCGCACCTACGTGCATTACCAGGATCCAAGCTCCAATTATCATTCCAACCCATGGTATTGAGCCCCTACAAATTTACTGAGAAAATAGTCAGGAAGAGCCGTAGGAATCAAGCCAACCGATCGACATGGTGCGGCAACACTCTCTGACCCCGTCCACCTACTAGGCTGCCCCCAGGTACACTGTGCCGAACGAGATTAGCGCAGAATTGGATTTCTGGTGCGATACTCTGGGCCAGCGGCGTTTTATATTTGAGCGGTCAAATAACTAGATGGTAACTATACTCGCCGATTGATTGGGTCACCTCGGGTCCCGTCTTTCAGCGCCTGCCTTAACTCATCCCCCTGAACGTGGATAAAAAAGTTAAGCCCATAGATGTGGTCAAAAACGAGAGTCAGAGGGCTCAATCAGACGGTGTTGGTCTGCGGAAGGGTTTGCAACTACTTATAGCCAGTTGTCCCAATCACCGCACCCGTAATCACAGAACACGTAGTCAAAGCCCTCCGGACTTCAGGTCGTACATGGCCCAAAAGTGTACTGCCGTACCTAAGTGAGACGGGGTGGTGGGGATTTCTCGGCACTAACTGGTCCCGGTGACTCAAGTTCGCGGCTCAAGCCAAGTTGACAATCGGGATTAGTGTTAGTAAGTAATTCAGATTGACGTAATGTGGGTCCAGAAACATTTCTAAAATCAACCTCCCGTCGATTTTCGGTGGACGGCCATTCGCGGTGACTACGCCATGCCCTTATGTTCTTGTTTGGAAAACTGACTCGATGAGCCGGGAGCTGAGACCGTGTAGAAGCGGCTGAGCCGTATCCGCCTAACTCTGTCACCAGATGCTGCGGAGGATTTACCGGTCCGCACCGAAGCCTTAATTCGATGAAGTAATGGCCGTGAAGCTAATCCGGGTCTATCCAGGGGAGCTCGCCGTTGGGTAACCATAGCCCCTGTACTATAAACGACGGTACAATACTCCTTGGTCGGCCGACGACCACTACGGCCGTCTGTTAGGGAAGTGGCAGAAACACGACCAACGCCGGGCTTTGGGTACTAACAGACGGCACGTGTAATACCTACGCTGAATAATGGGTTAAGAGTCTTAGTGTGGGCTTTCAAGGCAGCCCTTTCGCAGCTAGTCTGAACCTTGATTGGAGGAACCATCGATGTTAGATGGAGCTTGCCTGCCGCGGAAAACGCTGAATGATAATTGAGGCGTATATGGCAGGAGTTGTTTGACGAGCGGGCGGAGTACGGGGCAGCTAAGAACACTAGGACCGTCCGATGGCTGTCTAAGGGATTCTCGGAGAGCTTGTCGTGCAACATATGGTATAGTATACCTTATCTCTCCGCGAGTACGGAAAGAGTCGCCCCATACGGCTCTTCCAAGATTTGGGCGTTGAGAACGAGCTCCTCGGCGCGGTAAGTATTGGGCAGTATACCCGCCACTTGGGTGCACAATTTTCGTTCGGTGTCAATGCTCTATGACGCGGGTTATGACCACTATCAATCGCAGTACTAGGGATGTACCAGACACGGCCGCCTGGAGTGTGTGTAATTCAGTCTATTCTCGCGCCGATTGTAGGACGTGGACCAGAAGCTTCATCGACAATGTTTTCATTCGGTCAAGTGTTGGTTACTCGGATGAGAGCCCTGTTCCGATACATAGATATCTCCGATTTCGGCGTGATGGTATGTGCATGGATGCTCGCAAACTAAGCTCCCCCCCATGCCTTAGTAGTCTTGGCACCCACATACCGGCCCTAGCTCTGTAGAGCCCTCGGCTTATTTGTAATCTACCTGCCGTGGTGTATGATATTCGGTCAATAAGATAGGTGGCGGTGCCCAGGAACCCAACCACAAGTGCGCATGATTGGGCCTCGGTTCTCTTGGCCGAGATATTCATAGCATGGATCCTGCAGAGACTTCTATTACATATCATGCTGGGTTGTTTCCGGGTGGGTCATGATTGCGTGCTGACAGCTGTAATATAGAGTTAGATGGGGCATTTTGGATATAGGCCGTCAACCAGGTAGTTACGCTCGATGGGCCAAGTGCGCGTGGTTCATGGAGCCCGTCCTGTTAAGGTTACTCTGCGCGGACTCTAGGCACTATCTCCTCAAGGGTAAAAGCTGTGTCCACTTACTATCGATTATGTCTCAACCCGCAACAAAGATGATGTGCGTCAGCAGTTGCCAGACGCATTATGGCAGGGGGACTAGTGTAGGCTAAATGTCGAAGGTAGCAGCGCTTTCCGGCCCATCACGGGAAATCTCCCCACAATCTTGCTACAACCACGTAGTGTTGTAAGCCCAGCGACCCCGTAGTACCTCGCGACAATTAGGCTTGCGACAAGGCGAACGGTCCCTAGCGGCGTCTCTCTCATGGGGTCCAATCAAGAGCCGATGCCCACTGGAGCATTTATTCTGGCGAGGTTAATCCACACCTCTCTCTTAATGAGGCTCAACATTTGGGGGCCCTCTGGTCTCGCGAGGATTTTATGTCGGAGACTAAGGCGAATCACGCTCAGCTCCTCGGTCGTCGTCGGCTCATGCCAGCTGTAAGGCCTGTTATTTTGTTGCATTTGCTGTCGTGTACTAACGATACCCTAGTTCTCCACTTTAAGGTAGTGCCATCAACTAATGTCAACGACATGAATACTGAATAGAGAATCGCTCTCATCTCGCACGCTAACGGTACCACTAGCTTACAAGGCTACCGACACAAATCTCGACGTGCAATTAAAGAAACCCCCGATATGCACGTCCTGCGCTTGTAACCATAAAGGGGGTGTTACCCTCCTCCCTATAGTATAGTGCATGAGATGTCGGCGCAATTTATCAGCGCTGAAGCGCTGGGTGGTGGCTGTGTCTGTCTCTTGGGGCGTTATGCCGGTAAGTCGATACAAGTCGTCAGATGAGGTGCACACATTAGAACATGTAATCGCGGATTCGGGGTCGATCCTTTTAGGAGGTTTATGAAAGAGTAGCGGGTATATCTTAACTACCGGAATATTGTGACCGCTATCCCATACTGTCCGCTTCTGCAATAGAGATTCTAAGAAAGGAAACATGCCAGTGGTACACATGACACCCCTCGGTGCTCTTCTAGGTCCAATACTTTTACGTGTTCGCTCGGTCATGGTGCGATAACCGGTGAAGCTGGTGATGAAAGGCTGGGACAAGGTGCAACAATTCCCTAGTTCCGTATTTGGGTCATACGGTGAGCGTGCTGTAGTCCTCACCCGGTAAGTTTTGCACGCGCGAGAATCATCAATCTGTACCCCAGGTCAGAGTAACAACGACGAGGTACTTCCGGATCCTCATCGACACGTCTCATCGGGAACTTGTCCACGCGGCATGGATATAGCCCGAGGTTTTAGACAGCATCAAGAGAGGGCTGGCGTATGCCGGGCAAGTAGGATAAGACTATCTGCCATGACTGGTGAACGTCCAGGGGGGAGAGCCTTTATGACAAAATAAGATTTACGTCTACTTTCGTCCGATCGAAGAGTATGGATTCAATGGGCGTGAAGGTACTGCGTAAGGCGCGTTCATCTATATGATTGTCAAGAGTACCGGGAACTCGCGTTGGTCGGGCGGTAGACGCCAGATGTCTGGCCGAAAGTTCATCGATAATAAAGATGGAAGGTGTTAAGATGCCCATAAAACAAACGGAAGTTTCAGGGGGGGAAACGGGTTTATTATCAACCAGGCGTGCAGGTCATCCGGAAGGGGATTATCTTCGGACGTAGGCTATAATCTGCTGATCCATCCCAGTGGCACTTTAGTGGGCTATCGGTGGTAGTATAGACAGTCATTATGGACGATGGGTGACATATGGTCGTCCTTCCCAACTGCTTGTCGCGATCGGCGCCCCAAAACGGTATCTAGGCGGTTCTAAGGCGGTACCGCCAGTGATACCAATACGATATGCTCGACATTGAAACTGGCTCGCGCGACTTACCTTTGAGTGCCAGGACATAGTGGTAGCTGGGACCCGAATACGATTTAGGCAAGGCTGATGTTCTCTGTTTGAAAGCGCATTCCCGTCTCAACACACGCAGGACGGCTTTCAGTGGCGAAACGGGCCGAGTTCGCGCGTCCATAGGTCGGCTTCCTTGGATGTGTGATAGCATCATCCTCAAATATTACTTTCCCACACACATCGATGATGATGTGGGCCACACAGTATAAGACTGCATGCAAAAGTACAGTCGCCATCCCGCTCGTGGTGTCTCCTAAGTGTACCCTCATACAACCTTACCAGTTCCAAGTGTCGAAAGCGATCTGAGACCATAGGGCTAGCCGGACGGCCACCCCTTAGCAGCCATGGCGGTTTAAACACAATCAACCTTTCACACCCGATATAATGAAGGTTTTTGAATAACATGTCCGTGTAAGTAAACGGGGGGTCATAGGCACACTGCTGAGTGTAGAGGACGCAATATTTAAACCTAGGTCACACTCCCGAACCCGAGGTATCACTGGAGCTCTATCCCCGGTCAGTGGAGTGTCCGAGCGATCCTTTGTTGTATGTTGTCGGGAAAATATCATTTAGTCGTGGGTTGATACTATAGTCACTCTGTCCAGAGGGAATAGAGCAATTGAATTTGGCTTCACGGAGGAGTTGCTGAAACTTCCTTTTAAAGGGCATTTTTAGCGCCAGGAGGGAGGACACAGGCAGGTTTCATTCGCGACGATCGCGGAACCTCGTGGGAGGATAATTGTATACGGGTTATGCTTGGGGCGTCCCGCAGAGCGGACGACGGTCGCATGAGTGTTACCCTGACAACGCAAATTGTCTCGGCGTTGTTATGAGCTTCATGCGAAAGCTCGGGTAATTGACCAGACGCATGCGTACCGATATAAAGCACGTTGTGCCTGACTCCCTTAAATATCAAATACGATAGCAGACTTATCGCTCACAGACAGCTGAGACCCTTCAGACCACCGTACTTGGCACTGTCAGACGGTTCTGGCCATTCAATTCGGCGGGTCTAAAACTGCCGCCAGAGATCATAGGAACTTCCGTCACCGCGGGTCCTGTTGACCCAGGGAGAATTGCCAGGGCATTTAGCGAATCCTTAAATTCAGAATATCCCGACCGGTTCGGTTTAATAGGGAATATACGTCGCGTAAGCGCAGATAACAGTTTACCTCGCCCACGTTCTGGAGATCCATGTGTTGCAGCGGTAACTCGGATTCATAAACCTGGGGGCGAAGAGCCTCAAGCCGCCCAACGTAAATATGTGGTGGCCAACAAGACTGTGTATTCAAGCGCTTGATTAGTCTCACAGGCGAATGCTACCTGGACCACCGGGATGTCGCATGCGGAACGGGCGTGGATACCGAAATGTCTCGGAACGAGAACATCCGGATTCAGGACAGGCCGGAACATAGGCGTACAAGAAAGCAAGGTAGTACAGCGCGTTCTTGCCGTAGACAATGACGCTTCCACTCACTTGGCCTCGAATAGCACAAGCCTACATTGAATAATTACCTGCCTAGTCGAGTCATTTGGCACTCAACAGATCACGGAAGCCGCAATGCATAGACTTCCTGCAATCCCAGCCCCGCCTGTTTAAACTCCGAGGCTCGATGGGCGTGATTAAAGTTCACCAGACGTGTTCGGCT"
print('inversecomplement')
print(inversComplement(input))

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

Pattern = "CGTTGAACG"
Genome = "CGTTGAACGTTGAACGACGTTGAAGAGATATTTACCGTTGAACGTTGAATGCGTTGAAATGATCGTTGAACGTTGAACGTTGAAGGATTGAATCGTTGAATCGCGGCGTTGAATCGTTGAACGTTGAATGCCATCTTCGTTGAAATCCGTTGAAAGTAATGCGTTGAACCGTTGAACGTTGAACGTTGAAACGTTGAAACCCGTTGAAATCGTTGAACGTTGAACGTTGAAAATCGCGTTGAAATCACTCTTCCGTTGAACGTTGAAAGCGGGGAGCGTTGAATGGAAGATCGTTGAACGTTGAATCGTTGAAACAAACGTTGAACCCGTTGAACGTTGAATCCGTTGAACGTTGAATTGCCAGCTCCAGTTGCGTTGAACCGTTGAATCCGTTGAAGCCTCGTTGAAACGTTGAAAGCACGTTGAACTCCGTTGAAGGCGTTGAATTCGTTGAAATACGTTGAACGTTGAAGCGTTGAAAAAGTCGTTGAACGTTGAACGTTGAACATAAGCCCGTTGAACGCGTTGAAAACGTTGAACTCGTTGAATTATATCCCCGTTGAATGACGGGTCGTTGAACGTTGAAGACGTTGAACGTTGAACCGTTGAAACGTTGAATGAGACGTTGAACGTTGAAAGGCGTTGAATCTCGTTGAATACGCGGCGTTGAACAACCGTTGAACGTTGAAGCTCCGTTGAATAAGTCGTTGAATATACATGAGGCTGACGCGTTGAAAGACGTTGAAGTCGTTGAAGAACGTTGAACGTTGAATCGTTGAAGCCGTTGAACGTTGAAAGCTTGACGTTGAATGGGCGTTGAATATCCGTTGAAGAGCGTTGAAGACGTTGAAACCGTTGAAGCCTTTCCATCCGTTGAAGAGATGCTACGTTGAACGTTGAAACTTCGTTGAATAGAACGTTGAATCGTTGAAACGTTGAAACGACGTTGAAGAAACCGTTGAACGTTGAACGTTGAAGCGCGTTGAATCCGTTGAACGTTGAATTCGTTGAATTAAGCCGTTGAAGCGTTGAATCGTTGAATCCCGTTGAAACGCGTTGAACCAACCAGCGATTACGTTGAACTCCGTTGAACCGTTGAACGTTGAACGTTGAACGTTGAATCCGTTGAAATGAGTCGTTGAATACGTTGAACACGTTGAAGTTGCGTTGAAGTCCGTTGAACGTTGAACGTTGAAATGTCGTTGAACGTTGAAAACGTTGAACGTTGAATATCGTTGAACCGTTGAATTACACGTTGAACGTTGAAGGGAGCCCCCGTTGAACGATCGTTGAACCGTTGAATGTAGCCGTTGAAGTCGTTGAACGTTGAATCGTTGAACGTTGAACGACAAAAGCACTGCGTTGAAACGTTGAATAGTGCTCCCGTTGAATCATCACGTTGAACTCGTCCACACGTTGAAAACAACGTTGAAGCGTTGAAGTCGTTGAAATCGTTGAACAAACCACGTTGAACGTTGAACGTTGAACGTTGAAACGTTGAACGTTGAACGTTGAAATCGTTGAAGCGTTGAAGCGTTGAAACCGCGTTGAACTTATGCGTTGAACGTTGAACGTTGAAGCCGTTGAAATCCGTTGAAACGTTGAACCCGTTGAACCGTTGAACCGTTGAATCCCGTTGAACCGAAATCGCGTTGAAGAACGTTGAATGTCGTTGAAACGTTGAAAGCGTTGAACTCGTTGAACGTTGAACGTTGAACGTTGAACGTTGAATTGTCGCGACCCGTTGAACCGTTGAATCCGTTGAACCCGTTGAACGTTGAACGTTGAACGTTGAAGTCGTTGAAGATTCGTTGAATCTAGGCGTTGAACGTTGAACGTTGAACCGTTGAATGCGTTGAACGTTGAACCGTTGAAGGGACGTTGAACGTTGAAACGTTGAACGTTGAATTACCGTTGAAGCGTTGAAACGTTGAATGCGTTGAATCGTTGAAAGCGTTGAAAAGTCTTCGTTGAAGCGCCGTTGAATTCTACGGTGCGTTGAATACGTTGAACGTTGAATTAGAGTGCAACGTTGAACGTTGAACTCGTTGAACGTTGAAAACGTTGAAAGGTCCGTTGAAAACGCGTTGAACCGTTGAACCGTTGAACGTTGAATAGCGTTGAACGTTGAACCGTTGAAAGCGCGTTGAATCGCAGTCACGTTGAACGTTGAATCGTTGAACGTTGAAATGACGTTGAATCGTTGAAACGTTGAAGCGCCCTGGACCCCGTTGAACGTTGAAGGCATCTCGTTGAACGTTGAAACTCCGTTGAAGCGTTGAATTACGGGAACGTTGAACGTCGGCGACGTTGAATCGTTGAATCGTTGAACCGAAGGTCGTTGAATCGTTGAATTTGGCGTTGAAACGTTGAACCCGTTGAACGTTGAATCCGTTGAACGTTGAAGCCGTTGAACGTTGAACGTTGAATAAGACGTTGAACCGTTGAAATACGTTGAACGTTGAATCGTTGAACGTTGAAAGGTTGCCGTTGAATTCAGGCGTTGAACCCGTTGAACTTCGTTGAACGTTGAACGTTGAACGCGTTGAACGTTGAAAAAGCTACGTTGAATCGTTGAACAGGCCGTTGAACGTTGAACGTTGAATGGCCATGGTGGCTGCGTTGAATCGTTGAAAAAGGATTGGTACGTTGAAGCGTTGAAGGTGGGCGTTGAATTGACCCGTTGAACGTTGAACGTTGAACGTTGAATGGCGTTGAAGCCCGTTGAACGTTGAAGGGGCGTTGAATTCGTTGAACCCTTGTGCGTTGAACGTTGAACGTTGAACACGTTGAAATCGGCGTTGAATGCCGTTGAACGTTGAATGGCTACCGTTGAAGTAGCGTTGAACCTTCGACGTTGAACACGCGTTGAATACCGTTGAACGCGTTGAACGATTCGTTGAACGCCGTTGAACTAATTGTACGTTGAACGTTGAAGCCGTTGAATTCGTTGAAACCGTTGAACCGTTGAATGACGCCCTAATACAACGTTGAACGTTGAACCACCGCGTTGAACACGTTGAACCGACGTTGAACCCGTTGAATACCGTTGAAGGTCCCGTTGAAGCGTTGAAAAATTTCCGTTGAACCGTTGAACGTTGAACCCGTTGAAGCGTTGAATATGCGATACTCGTCGTTGAACGTTGAAGAATCTGCGTTGAACACGTTGAACGTTGAATCGTTGAACGTTGAATGCGTTGAAACCCTGCGTTGAAGCGTTGAAAACAGGCGTTGAACGTTGAAGAACTGACGTTGAAGCGTTGAACGCGGCGTTGAACGTTGAACGTTGAACGTTGAATCGTTGAAACTTCGTTGAAATGCGTTGAACGTTGAACGTTGAAACCGATTCGTTGAAACCGCGTTGAACCGCCGTTGAACGTTGAAGTGGCGTTGAAGGAAATCGTTGAAAACCGTTGAAGTCGCGTTGAAACAATGCGTTGAACAATGGGGATCGTTGAACGTTGAACGTTGAACGTTGAACCTCGTTGAAACTCGTTGAACGTTGAACGTTGAAAAGCCGTTGAACCCCCGTTGAAACGTTGAATCCAATCTCGTTGAATACTCCGTTGAAGGTATCGTTGAATCGTTGAACGTTGAACGTTGAACCCGTTGAATCGTACGTTGAATTCTCTCGTTGAAAGCGTTGAACGTTGAACAAGTCATATTCGTTGAACGTTGAACGTTGAAACGTTGAAGCGTTGAACGTTGAACGTTGAATATCGTTGAACGTTGAATACGTTGAATGCCGTTGAACAGCTAGCCCGTTGAACCCACAAGCTCGTTGAACGTTGAACGACGTTGAAATAGACGTTGAACGCGTTGAACGTGTCGTTGAAGCGTTGAACGTTGAACCGTTGAAAAACGTTGAAACGTTGAAACGTTGAACTTCGTTGAAGAGACGACGTTGAAGACGTTGAACGTTGAAATGCGTTGAACAGCGTTGAAGCGTTGAAACGTTGAATCGTTGAACAACCCGTTGAAACCACGTTGAAGCGAACCGTTGAATCGTTGAAATGGACCCGTTGAAGGGCGTTGAACAGATCTGCCGTTGAACGTTGAAAACTCCGTTGAATTGACGTGACGTTGAACGTTGAACGTTGAACGTTGAAATCGCGTTGAAGCCCGTTGAATTACACAATTTTACGTTGAACGTTGAACGTTGAAGCGTTGAATCGTTGAACGTTGAATCCGTTGAATCGTTGAACTCGTTGAACGTTGAAACCGTTGAACGTTGAAGCGTCGTTGAATCGTTGAACGTTGAAAACGCGTTGAATAACGTTGAATCCCATCTGGGCGTTGAACGTTGAATCGATCGTTGAAATCCGTTGAAAGCGTTGAATCCGTTGAATAGCTTCGTCTCGTTGAAGCGTTGAACGTTGAAGATCTTCGTTGAACGTTGAACTTCGTTGAAGCGTTGAAGACGTTGAAAAGAATCGTTGAATTCGTTGAAAATCCGTTGAACCGTTGAACGTTGAACGTTGAAGGCGTTGAAACGTTGAACCCCACGTTGAACGTTGAACGTTGAATCGTTGAATAAACGTTGAAGGTTTCCGTTGAAAATAACGTTGAAGCGTTGAAACGTTGAAATCGTTGAATCGTTGAACACGTTGAACTCGTTGAAGGCGTTGAACGTTGAAACCTGCGTTGAAATCCGTTGAACGTTGAAGCATCGACGTTGAAAGCCACAGCCGTTGAATCGTTGAATGCGTTGAACGTTGAACATCCACCGTTGAAACAACGTTGAATAAAACAGTTTCGTTGAATGCGTTGAACGTTGAACCGTTGAAGATTGCGTTGAAACCGTTGAATGCCCGTTGAAGCGTTGAAGGCAGCCACGTTGAATCTTCCTAACGTTGAAGTAACGTTGAAAGGCGTTGAATACACAACCGCATCCGTTGAAATTCGTTGAACGTTGAACGTTGAATCAACGTTGAATCTATCGTTGAATCGTTGAACGGTCAGCGTTGAACGTTGAAGCGTTGAACAGCTCGTTGAACGTTGAAGTCGTTGAAGCGTTGAATCGCGTTGAAGCCGTTGAAATGATTCGTTGAATGGCCGATCCGTTGAACGTTGAAAGGCGTTGAATCACGTTGAACGTTGAAAGGACGTTGAAACGTTGAACGTTGAACGTTGAACGTTGAACCGCGTTGAACTCCTCGTTGAATCGTTGAACCGTTGAAGCCGTTGAACACGCGTTGAAGCGTACGTTGAACGTTGAAACGTTGAACGTTGAATGTTTAAAGTCGTTGAACGTTGAAACGTTGAAGAGCCGTTGAATTACGTTGAATGCGTTGAAAAGGGCGACGTTGAAGGTCGTTGAAAACGTTGAACCGTTGAACCTCGTTGAACCGTTGAATACGTTGAATCGTTGAAACATAGCGTTGAACGTTGAATTGAGCGTTGAACCGTTGAAACGTTGAATTCGCGTTGAATCGTTGAATGCGCCCGTTGAACCGGAGTGTGCGTTGAACGAATACTTGTAATCCGTTGAAGCGTTGAAGCGTTGAACGTTGAAAGACCGTTGAATTGCCGTTGAAAGGCGTCGTTGAATCGTTGAAATTACAATGTAGCGTTGAATCGTTGAACCCGTTGAAACCGTTGAACGTTGAATTTAGCGTTGAAACTCCCCGTTGAAAGAGCCGTTGAAGGAACGTTGAATAGACGTTGAAGATGGGGCGTTGAATAGTTTACAGCCGGCCCCGTTGAATCGTTGAAGGCTTTTGCGGCGTTGAATGCGTTGAATGCCGTTGAAGGGGCGTTGAACGAGCGTTGAACCGTTGAAGCGCGCGTTGAAAAGTTTTCGTTGAATCGTTGAACGTTGAACGTTGAAAGCAGTCGTTGAAACGTTGAACGTTGAAGCGTTGAACAACGTTGAACGTTGAAATTCCGTTGAAGCACGTTGAACGTTGAACCCGTTGAAGCCGTTGAACGTTGAAGCGTTGAACGTTGAAGCGTTGAACCCCCGTTGAATCCGTTGAACAGCGTTGAACCGTTGAATAGCGTTGAAGAAGTTTATCGTTGAATAACGGCACGTTGAAATTGCGTTGAACGTTGAAAGCCGACGATTCAGCGTTGAACGTTGAATCTGTTCGTTGAACCACGTTGAAATAACGTTGAAGCGTTGAATCATTGTCCCACGTTGAAGGGTCCCGTTGAAGTTTCCCGTTGAATGCGTTGAATTCGTTGAAGCTTCACACGTTGAAACGTTGAATTGCGTTGAAGCGTTGAAGGATTAAGACGTTGAAACGTTGAATCGTTGAACGTTGAACGTTGAACACAACGTTGAACGTTGAAAACGTTGAACTTCGTTGAATAGCACGTTGAACGTTGAACGTTGAAGTAAGAACCGTTGAATACGTTGAAAGCGCGTTGAACGCGTTGAATGGTCGTTGAACCGTTGAACGTTGAAAAAGCGTTGAATCGTTGAAGACCGTTGAACGTTGAACCGTTGAAATCGTTGAAGCGTTGAACGTTGAAATCCGTTGAATTCTGCTGCCCGTTGAACGTCGTTGAAAGGTTACGTTGAAGGCGTTGAACACGTTGAATTCCCTAGCGTTGAAACGTTGAATCGTTGAAGCCCAACGTTGAAACGTTGAAGTGCGTTGAAGTGACACATCGTTGAAGCATTCGTTGAAAGCGTTGAAGGCGTTGAACGTTGAAAAGGGACGTTGAACGTTGAACGTTGAACTCGCGTTGAACGTTGAAGAGCCGTTGAAGACGTTGAACGTTGAAGGTACGTTGAAAAAGGCGTTGAACCCGTTGAAGCCGTTGAACCGTTGAAACGTTGAACGTTGAATTGATACGTTGAATCGTTGAACGTTGAATAGTCGTTGAAAAGGCGTTGAACGCCCGTTGAACGTTGAAACCCGTTGAACGTTGAAGTGAGTCGTTGAAGCCGTTGAAACGCACGTTGAAGGCGTTGAACGCACCACCGTTGAACGTTGAAGACGTTGAATCCGTTGAAGAAACGTTGAATCGTTGAATGGGCGTTGAACGTCGTTGAAGACGTTGAATGCACGTTGAAGACCGTTGAACGTTGAACGTTGAAACCCCCAACCGTTGAAGGGTCGTTGAAGCTTCGTTGAAACGTTGAAAAGTGCACCGTTGAACGTTGAATTCCGTTGAACGTTGAAGGTTCGTTGAAACGTTGAACTCGTTGAACATTATCGTTGAACGGCGGCGTTGAAAGCGTTGAAGGCGTTGAAGGACTTAAACTGTACGTTGAACGTTGAAGCGTTGAACGTTGAACGTTGAACGTTGAATCGTTGAAAGAAGGAGAGTACGTAACCGTTGAACCAGACCGTTGAACTCGTTGAAACGTTGAACGTTGAAGCTCGTTGAAGAGCGTTGAATAGCCGTTGAAGGCTCCGTTGAAGTCGGCGTTGAATCGTTGAACACCGTTGAAGTTTCGTTGAACGTTGAACGTTGAACGTTGAACACGTTGAAGCACGTTGAATGTGCGTTGAACACACGTTGAAGTAATAAGATACAGGCTACGTTGAAGCGCCGTTGAACTCCGTTGAACGTTGAACGTTGAACGTTGAACGTTGAAACGTTGAAGCCTCTCGTTGAAACTGACGTTGAACGTTGAATAGAACGTTGAACACGATTGCCGTTGAAATCGTTGAAACAGAACACGTTGAAGCCGTTGAAACCGCGTTGAATCCTTCGTTGAAACGTTGAAGCGTTGAACAGTCGTTGAACACGTTGAATCGTTGAAGACGCGTTGAAGACGTTGAATTTTGTTCTTACTCGTTGAACGTTGAATAGGGTATCGTTGAAGCTTCTGCGTTGAAACTCGTTGAACGTTGAAGCGCGGGAGATTCGTTGAAACGTTGAAACGTTGAACGTTGAAGGCGCGTTGAAGGTAGACGTTGAACGTTGAATAAGCTGCCAGTCGTTGAACGTTGAACGTTGAACGTTGAAACGTTGAATTTACGTTGAATCTCGTTGAAATGCGTTGAACGTTGAAACAATCGTTGAACGTTGAAACTCAACAAACGTTGAAGTTCGTTGAACCGTTGAACGTTGAACGTTGAACGTTGAAGAGCGTTGAACGTTGAAGCGTTGAACCGTTGAAAGCGTTGAAAGTCCGTTGAATGTAACGTTGAACGTTGAAAGCGTTGAACGTACGTTGAACGTTGAACCGTTGAAATCGTTGAATGCGTTGAACGCGTTGAAAAAGACGTTGAAACGTTGAATACGTTGAACGTTGAACGTTGAAACCCGTTGAACGTTGAAGAGTTATACGTTGAAACCGTTGAACGTTGAAAACGTTGAACGTTGAATGAGACGTTGAAGCGTTGAAAGGGTATTCCGTTGAATCGTTGAACCGTTGAATCGTTGAACGCGTTGAACGGGCCGTTGAACTAGTGACGTTGAACGTTGAATTTATCGTTGAAACTACGTTGAATTGATTTCGTTGAATACGTTGAAGAACCGTTGAACGTTGAACGTTGAAGATCGCGTTGAACCGTTGAAATCGTTGAATAGCCGTTGAATCGTTGAACGTTGAACGTTGAACGTTGAACTTGA"
genome = Genome
print(PatternMatching(Pattern, Genome))
print('PatternMatching')
oriC = "aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggttt"


def kmerPositions(k, sequence):
    """ returns the position of all k-mers in sequence as a dictionary"""
    kmerPosition = {}
    for i in range(1, len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmerPosition[kmer] = kmerPosition.get(kmer, []) + [i]
    # combine kmers and their reverse complements
    pairPosition = {}
    for kmer in iter(kmerPosition.keys()):
        krev = ''.join([{'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}[base] for base in reversed(kmer)])
        if (krev in kmerPosition):
            if (kmer <= krev):
                pairPosition[kmer] = kmerPosition[kmer] + kmerPosition[krev]
        else:
            if (kmer <= krev):
                pairPosition[kmer] = kmerPosition[kmer]
            else:
                pairPosition[krev] = kmerPosition[kmer]
    return pairPosition


def findClumps(string, k, L, t):
    clumps = []
    kmers = kmerPositions(k, string)
    for kmer, posList in kmers.items():
        i = 0
        while (i < len(posList) - t - 1):
            foundSoFar = 1
            for j in range(i + 1, len(posList)):
                if (((posList[j] + k) - posList[i]) > L):
                    break
                foundSoFar += 1
            if (foundSoFar >= t):
                clumps.append((kmer, foundSoFar))
            i = j
    return clumps

def kmerFreq(k, sequence):
    """ returns the count of all k-mers in sequence as a dictionary"""
    kmerCount = {}
    for i in range(len(sequence)-k+1):
        kmer = sequence[i:i+k]
        kmerCount[kmer] = kmerCount.get(kmer,0)+1
    return kmerCount

K = 9
L = 500
T = 6

print("Here is your Clump List")
clumpList = findClumps(genome, K, L, T)
print(len(clumpList))
print(clumpList[i] for i in range(min(10, len(clumpList))))

for k in range(1,10):
    kmerCounts = kmerFreq(k,oriC).items()
    kmerCounts = sorted(kmerCounts,reverse=True,key=lambda tup: tup[1])
    mostFreq = []
    most = kmerCounts[0][1]
    for kmer, count in kmerCounts:
        mostFreq.append((kmer, count))
        if count != most:
            break
    print(k, mostFreq)