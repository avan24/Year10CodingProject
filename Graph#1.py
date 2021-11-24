GPA = loadList('GPA.csv')

colors = ['crimson','wheat', 'royalblue', 'darkorange', 'darkgreen', 'grey', 'gold', 'mediumaquamarine', 'darkviolet', 'midnightblue']


#get the values from the row and column [row][column]
dataOnly = []
for i in range (1,len(GPA)):
    dataOnly+=[[GPA[i][0],float(GPA[i][1]), float(GPA[i][2])]]
#print (dataOnly)

#the name of the list is "dataOnly" it creates a list using the columns "School", "Acceptance Rate", and "GPA"
df = pd.DataFrame(dataOnly, columns = ['School', 'Accept', 'gpa'])


plt.scatter(Harvard_AR, Harvard_GPA, marker='o', color=colors[0],label='Harvard University (HU)')
plt.scatter(Stanford_AR, Stanford_GPA, marker='o', color=colors[1],label='Stanford University (SU)')
plt.scatter(UCLA_AR, UCLA_GPA, marker='o', color=colors[2],label='University of California Los Angeles (UCLA)')
plt.scatter(UVA_AR, UVA_GPA, marker='o', color=colors[3],label='University of Virginia (UVA)')
plt.scatter(UF_AR, UF_GPA, marker='o', color=colors[4],label='University of Florida (UF)')
plt.scatter(OSU_AR, OSU_GPA, marker='o', color=colors[5],label='Ohio State University (OSU)')
plt.scatter(USF_AR, USF_GPA, marker='o', color=colors[6],label='University of Florida (UF)')
plt.scatter(MSU_AR, MSU_GPA, marker='o', color=colors[7],label='Michigan State University (MSU)')
plt.scatter(LSU_AR, LSU_GPA, marker='o', color=colors[8],label='Louisiana State University (LSU)')
plt.scatter(CU_AR, CU_GPA, marker='o', color=colors[9],label='Clarke University (CU)')



plt.gca().invert_yaxis()

# specific location of legend (ncol = 1 means the number of columns in the legend)
plt.legend(loc='upper center', bbox_to_anchor=(1.4, 1), fancybox=True, shadow=True, ncol=1)

plt.xlim(0, 100)
plt.ylim(3, 4.5)


plt.title("Average GPA vs Acceptance Rate", horizontalalignment='center', verticalalignment='top', fontweight='bold', fontsize='15', pad=0)

plt.xlabel('Acceptance Rate (%)', fontsize='13')
plt.ylabel('GPA (Weighted)', fontsize='13')


# Find the trend line data points using polyfit() and poly1d() method.
z = np.polyfit(df.Accept, df.gpa, 1)
p = np.poly1d(z)
#Plot x and p(x) data points using plot() method.
plt.plot(df.Accept, p(df.Accept), "k")


plt.show()

