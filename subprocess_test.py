'''
Created on Dec 3, 2014

@author: jimhorng
'''

import subprocess

def cms_sign_data(data_to_sign, signing_cert_file_name, signing_key_file_name,
                  outform=PKI_ASN1_FORM):
    """Uses OpenSSL to sign a document.
    Produces a Base64 encoding of a DER formatted CMS Document
    http://en.wikipedia.org/wiki/Cryptographic_Message_Syntax
    :param data_to_sign: data to sign
    :param signing_cert_file_name:  path to the X509 certificate containing
        the public key associated with the private key used to sign the data
    :param signing_key_file_name: path to the private key used to sign
        the data
    :param outform: Format for the signed document PKIZ_CMS_FORM or
        PKI_ASN1_FORM
    """
    _ensure_subprocess()
    if isinstance(data_to_sign, six.string_types):
        data = bytearray(data_to_sign, encoding='utf-8')
    else:
        data = data_to_sign
    process = subprocess.Popen(['openssl', 'cms', '-sign',
                                '-signer', signing_cert_file_name,
                                '-inkey', signing_key_file_name,
                                '-outform', 'PEM',
                                '-nosmimecap', '-nodetach',
                                '-nocerts', '-noattr',
                                '-md', 'sha256', ],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               close_fds=True)

    output, err, retcode = _process_communicate_handle_oserror(
        process, data, (signing_cert_file_name, signing_key_file_name))

    if retcode != OpensslCmsExitStatus.SUCCESS or ('Error' in err):
        if retcode == OpensslCmsExitStatus.CREATE_CMS_READ_MIME_ERROR:
            LOG.error(_LE('Signing error: Unable to load certificate - '
                          'ensure you have configured PKI with '
                          '"keystone-manage pki_setup"'))
        else:
            LOG.error(_LE('Signing error: %s'), err)
        raise subprocess.CalledProcessError(retcode, 'openssl')
    if outform == PKI_ASN1_FORM:
        return output.decode('utf-8')
    else:
        return output

def _process_communicate_handle_oserror(process, data, files):
    """Wrapper around process.communicate that checks for OSError."""

    try:
        output, err = process.communicate(data)
    except OSError as e:
        if e.errno != errno.EPIPE:
            raise
        # OSError with EPIPE only occurs with Python 2.6.x/old 2.7.x
        # http://bugs.python.org/issue10963

        # The quick exit is typically caused by the openssl command not being
        # able to read an input file, so check ourselves if can't read a file.
        retcode, err = _check_files_accessible(files)
        if process.stderr:
            msg = process.stderr.read()
            err = err + msg.decode('utf-8')
        output = ''
    else:
        retcode = process.poll()
        if err is not None:
            err = err.decode('utf-8')

    return output, err, retcode

def main():
    pass

if __name__ == "__main__":
    main()