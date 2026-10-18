"""Unit tests for SkinBuilder and Showcase Renderer."""

import unittest
from pathlib import Path
from PIL import Image

import sys
scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

from skin_builder import SkinBuilder
from skin_tools import validate_skin


class TestSkinBuilder(unittest.TestCase):

    def test_init_and_blank_validation(self):
        builder = SkinBuilder(model='slim')
        val = builder.validate()
        self.assertTrue(val['passed'])
        self.assertEqual(val['model'], 'slim')
        self.assertEqual(val['errors'], [])

    def test_set_face_valid(self):
        builder = SkinBuilder(model='slim')
        gold = (255, 215, 0, 255)
        builder.fill_face('head.top', 'outer', gold)
        val = builder.validate()
        self.assertTrue(val['passed'])
        # Verify pixels were written
        bx, by, bw, bh = builder.faces['head.top']['outer']
        self.assertEqual(builder.image.getpixel((bx, by)), gold)

    def test_invalid_dimensions_rejected(self):
        builder = SkinBuilder(model='slim')
        with self.assertRaises(ValueError):
            # Head front is 8x8, passing 4 rows should fail
            builder.set_face('head.front', 'base', [[(0,0,0,255)]*8]*4)

    def test_save_and_reload(self):
        import tempfile
        builder = SkinBuilder(model='slim')
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = Path(tmpdir) / "test_skin.png"
            builder.save(out_path)
            self.assertTrue(out_path.exists())
            img = Image.open(out_path)
            self.assertEqual(img.size, (64, 64))
            val = validate_skin(img, 'slim')
            self.assertTrue(val['passed'])


if __name__ == '__main__':
    unittest.main()
