
import enum

@enum.unique
class MobileMoneyProviders(enum.Enum):
    ACLEDABANK_KH = object()
    AFRICELL_SL = object()
    AIRTEL_KE = object()



provider = MobileMoneyProviders.ACLEDABANK_KH
print(provider.name)
# print(type(provider.name))
# print(type(MobileMoneyProviders.ACLEDABANK_KH))
# print(MobileMoneyProviders.ACLEDABANK_KH)
# print(MobileMoneyProviders.ACLEDABANK_KH.name)
print(str(MobileMoneyProviders.ACLEDABANK_KH.name))
# print(type(MobileMoneyProviders.ACLEDABANK_KH.name))




class OrganizationType(enum.Enum):
    DISTRIBUTOR = object()
    MERCHANT = object()
    CLIENT_CARE_PROVIDER = object()


print(OrganizationType.MERCHANT.name)



