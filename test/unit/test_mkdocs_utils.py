import os
import subprocess
import unittest
from unittest import mock

from .. import *
from mike import utils


class TestLoadConfig(unittest.TestCase):
    def test_default(self):
        os.chdir(os.path.join(test_data_dir, 'basic_theme'))
        cfg = utils.load_config()
        self.assertIsNotNone(cfg)

    def test_abs_path(self):
        path = os.path.join(test_data_dir, 'basic_theme', 'zensical.toml')
        cfg = utils.load_config(path)
        self.assertIsNotNone(cfg)

    def test_nonexist(self):
        os.chdir(os.path.join(test_data_dir, 'basic_theme'))
        with self.assertRaisesRegex(FileNotFoundError, r"'nonexist.toml'"):
            utils.load_config('nonexist.toml')
        with self.assertRaisesRegex(FileNotFoundError, r"'nonexist.toml'"):
            utils.load_config(['nonexist.toml', 'nonexist2.toml'])

        cfg = utils.load_config(['nonexist.toml', 'zensical.toml'])
        self.assertIsNotNone(cfg)


class TestInjectPlugin(unittest.TestCase):
    def test_passthrough(self):
        path = os.path.join(test_data_dir, 'basic_theme', 'zensical.toml')
        with utils.inject_plugin(path) as f:
            self.assertEqual(f, path)

    def test_missing(self):
        with self.assertRaises(FileNotFoundError):
            with utils.inject_plugin('nonexist.toml'):
                pass


class TestBuild(unittest.TestCase):
    def test_build(self):
        with mock.patch('subprocess.run') as mrun:
            utils.build('zensical.toml', '1.0', output=subprocess.DEVNULL)
        mrun.assert_called_once()
        args = mrun.call_args[0][0]
        self.assertEqual(args[:3], ['zensical', 'build', '--clean'])
        self.assertIn('zensical.toml', args)
        env = mrun.call_args[1]['env']
        self.assertEqual(env[utils.docs_version_var], '1.0')


class TestVersion(unittest.TestCase):
    def test_version(self):
        self.assertRegex(utils.version(), r'\S+')
