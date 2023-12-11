def test_prospect__with_used_national_id_in_distributor_org__returns_false(
        self
    ):
        self.do_setup_wrapper()
        # create an existing locked account in distributor organization
        org_one = self.fake.unique_organization()
        user = self.fake.unique_user(organization=org_one)

        client = self.fake.client(
            organization=org_one, recorder=user, id_number=NATIONAL_ID_NUMBER
        )
        account = self.fake.account(
            organization=org_one, is_activated=True, client=client
        )
        biz.commit()
        assert_is_not_none(account)
        assert_equal(False, account.is_unlocked)
        assert_equal(client, account.customers[0])
        assert_equal(client.id_number, NATIONAL_ID_NUMBER)
        assert_equal(account.organization.type, OrganizationType.DISTRIBUTOR)

        # now create a new prospect
        user = self.fake.unique_user(
            organization=self.org,
            all_registration_groups=True,
            primary_phone="+15551234568",
        )
        biz.flush()
        prospect = self._start_prospect()
        prospect.update(user, fields=self._get_fields())
        biz.commit()

        response = self._client.get(
            self.url(".underwriting_has_existing"),
            query_string=dict(prospect_qid=prospect.qid),
        )
        assert_equal(response.status_code, 200)
        media = za.util.dejsonify(response.data)
        expected_response = {"has_existing_account": False}
        assert_equal(expected_response, media)




















def do_set_wrapper(self, is_mercant=True, trans_reg_inputs=lambda y:y):
    self.do_setup(
        reg_inputs = trans_reg_inputs(
            [
                {
                    "customer_first_name": dict(
                        is_enabled=True,
                        registration_type=(
                            RegistrationInputRegistrationType.PROSPECTS
                        ),
                    )
                },
            ]
        )
    )


bulbs = lam

