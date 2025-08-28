# List of usernames
users=(
almusty2impact
emmanueleyo023
mairogreat
davidadinnu
Akinsolagideonn
robertzerah
gbadamosifatimah01
ijeteoluwatobi
Ubarajf
onihunwaa
ibehamarachi18
hifeally
obiefunadimz
andealexis12
egunjobiayooluwa
eneuneochedi
infoaboutgideon
ezinne.emegharaibe
badmusibrahimadewale01
francisadedejiayo
blessingisoken97
adeeyoabdulgafar
Andrewemmanuel416
onyinye.ogbonna.maryjane
tosinobateru01
onwuteakadavid
akandegbolahanayomide
harrisoncovenant
fridayks96
hildajack16
akintayoabidemitope
ijeomareaganok
jessetak
oridami49
echinnannachukwuemeka
osuagwuucheoma
euniceobasanmi
daniellachukwu772
Chinwekeleanthony
adamsunday39
moyindanisi
felixchukwuemeka64
similoluwaoluwatomisin
olawaleajibola30
Shodeindesimeon
johnadejumo93
omagbemimogbeyi
)

# Loop through all section directories
for section in day1/section-*; do
  for user in "${users[@]}"; do
    mkdir -p "$section/$user"
  done
done
