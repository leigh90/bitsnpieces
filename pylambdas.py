x = lambda a : a + 10
y = lambda a,b : a * b
z = lambda a,b, c : (a*c)//b

print(x(5))
print(y(5,8))
print(z(10,5,7))

red_panda = lambda x:x
reg_inputs = red_panda(
    [{
        "customer_first_name": dict(
            is_enabled=True,
            registration_type=(
                "RegistrationInputRegistrationType.PROSPECTS"
            ),
        )
    },
    {
        "customer_last_name": dict(
            is_enabled=True,
            registration_type=(
                "RegistrationInputRegistrationType.PROSPECTS"
            ),
        )
    },]
)
print(reg_inputs)



