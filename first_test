class TestJobCredentials(TestJobExecution):

    parametrize = {
        'test_ssh_passwords': [
            dict(field='password', password_name='ssh_password', expected_flag='--ask-pass'),
            dict(field='ssh_key_unlock', password_name='ssh_key_unlock', expected_flag=None),
            dict(field='become_password', password_name='become_password', expected_flag='--ask-become-pass'),

    def test_become_method(self, field, password_name, expected_flag):
        ssh = CredentialType.defaults['ssh']()
        credential = Credential(
            pk=1,
            credential_type=ssh,
            inputs = {'username': 'bob', field: 'secret', become_method: 'doas'}
        )
        credential.inputs[field] = encrypt_field(credential, field)
        self.instance.credentials.add(credential)
        self.task.run(self.pk)

        assert self.run_pexpect.call_count == 1
        call_args, call_kwargs = self.run_pexpect.call_args_list[0]
        args, cwd, env, stdout = call_args

        assert '-u bob' in ' '.join(args)
        assert 'secret' in call_kwargs.get('expect_passwords').values()
        assert '--become_method doas' in ' '.join(args)
        if expected_flag:
            assert expected_flag in ' '.join(args)
