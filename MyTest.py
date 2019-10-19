import unittest
import YT2TVDB


class MyTestCase(unittest.TestCase):
    def test_different_youtube_url_formats(self):
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/attribution_link?a=8g8kPrPIi-ecwIsS&u=/"
                                      "watch%3Fv%3DyZv2daTWRZU%26feature%3Dem-uploademail", "maxres"),
            "https://i.ytimg.com/vi/yZv2daTWRZU/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://youtu.be/yZv2daTWRZU", "maxres"),
            "https://i.ytimg.com/vi/yZv2daTWRZU/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/watch?v=0I6ZQOPfgJk", "maxres"),
            "https://i.ytimg.com/vi/0I6ZQOPfgJk/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/watch?v=0I6ZQOPfgJk ", "maxres"),
            "https://i.ytimg.com/vi/0I6ZQOPfgJk/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/"
                                      "watch?v=0I6ZQOPfgJk&index=1&list=PL2EJlPZ0iJu6InkJI0GyoFoFkReYWB3h7", "maxres"),
            "https://i.ytimg.com/vi/0I6ZQOPfgJk/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/watch?v=tlTKTTt47WE&index=1&list=WL&t=14s", "maxres"),
            "https://i.ytimg.com/vi/tlTKTTt47WE/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url(
                "https://www.youtube.com/watch?v=zNfK-YqLUbU&list=FLGdHxhoePBkfbI6lIdhFFXw&index=1&t=32s", "maxres"),
            "https://i.ytimg.com/vi/zNfK-YqLUbU/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url(
                "https://www.youtube.com/watch?v=bvim4rsNHkQ&t=23s&list=LLGdHxhoePBkfbI6lIdhFFXw&index=1", "maxres"),
            "https://i.ytimg.com/vi/bvim4rsNHkQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/watch?v=-wtIMTCHWuI", "maxres"),
            "https://i.ytimg.com/vi/-wtIMTCHWuI/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/v/-wtIMTCHWuI?version=3&autohide=1", "maxres"),
            "https://i.ytimg.com/vi/-wtIMTCHWuI/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtu.be/-wtIMTCHWuI", "maxres"),
            "https://i.ytimg.com/vi/-wtIMTCHWuI/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url(
                "http://www.youtube.com/oembed?url=http%3A//www.youtube.com/watch?v%3D-wtIMTCHWuI&format=json", "maxres"),
            "https://i.ytimg.com/vi/-wtIMTCHWuI/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/embed/M7lc1UVf-VE", "maxres"),
            "https://i.ytimg.com/vi/M7lc1UVf-VE/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url(
                "http://www.youtube.com/attribution_link?a=JdfC0C9V6ZI&u=%2Fwatch%3Fv%3DEhxJLojIE_o%26feature%3Dshare", "maxres"),
            "https://i.ytimg.com/vi/EhxJLojIE_o/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/watch?v=yZv2daTWRZU&feature=em-uploademail", "maxres"),
            "https://i.ytimg.com/vi/yZv2daTWRZU/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/watch?v=tlTKTTt47WE&index=2&list=WL", "maxres"),
            "https://i.ytimg.com/vi/tlTKTTt47WE/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/watch?v=0zM3nApSvMg&feature=feedrec_grec_index", "maxres"),
            "https://i.ytimg.com/vi/0zM3nApSvMg/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/user/IngridMichaelsonVEVO#p/a/u/1/QdK8U-VIH_o", "maxres"),
            "https://i.ytimg.com/vi/QdK8U-VIH_o/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/v/0zM3nApSvMg?fs=1&amp;hl=en_US&amp;rel=0", "maxres"),
            "https://i.ytimg.com/vi/0zM3nApSvMg/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/watch?v=0zM3nApSvMg#t=0m10s", "maxres"),
            "https://i.ytimg.com/vi/0zM3nApSvMg/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/embed/0zM3nApSvMg?rel=0", "maxres"),
            "https://i.ytimg.com/vi/0zM3nApSvMg/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("//www.youtube-nocookie.com/embed/up_lNV-yoK4?rel=0", "maxres"),
            "https://i.ytimg.com/vi/up_lNV-yoK4/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube-nocookie.com/embed/up_lNV-yoK4?rel=0", "maxres"),
            "https://i.ytimg.com/vi/up_lNV-yoK4/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/user/Scobleizer#p/u/1/1p3vcRhsYGo", "maxres"),
            "https://i.ytimg.com/vi/1p3vcRhsYGo/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/watch?v=cKZDdG9FTKY&feature=channel", "maxres"),
            "https://i.ytimg.com/vi/cKZDdG9FTKY/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url(
                "http://www.youtube.com/watch?v=yZ-K7nCVnBI&playnext_from=TL&videos=osPknwzXEas&feature=sub", "maxres"),
            "https://i.ytimg.com/vi/yZ-K7nCVnBI/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/ytscreeningroom?v=NRHVzbJVx8I", "maxres"),
            "https://i.ytimg.com/vi/NRHVzbJVx8I/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/watch?v=6dwqZw0j_jY&feature=youtu.be", "maxres"),
            "https://i.ytimg.com/vi/6dwqZw0j_jY/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/user/Scobleizer#p/u/1/1p3vcRhsYGo?rel=0", "maxres"),
            "https://i.ytimg.com/vi/1p3vcRhsYGo/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/embed/nas1rJpm7wY?rel=0", "maxres"),
            "https://i.ytimg.com/vi/nas1rJpm7wY/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://www.youtube.com/watch?v=peFZbP64dsU", "maxres"),
            "https://i.ytimg.com/vi/peFZbP64dsU/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/v/dQw4w9WgXcQ?feature=youtube_gdata_player", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/?v=dQw4w9WgXcQ&feature=youtube_gdata_player", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtube_gdata_player", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/?vi=dQw4w9WgXcQ&feature=youtube_gdata_player", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/watch?v=dQw4w9WgXcQ&feature=youtube_gdata_player", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/watch?vi=dQw4w9WgXcQ&feature=youtube_gdata_player", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/vi/dQw4w9WgXcQ?feature=youtube_gdata_player", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtu.be/dQw4w9WgXcQ?feature=youtube_gdata_player", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/user/SilkRoadTheatre#p/a/u/2/6dwqZw0j_jY", "maxres"),
            "https://i.ytimg.com/vi/6dwqZw0j_jY/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url(
                "https://www.youtube.com/watch?v=ishbTyLs6ps&list=PLGup6kBfcU7Le5laEaCLgTKtlDcxMqGxZ&index=106"
                "&shuffle=2655", "maxres"),
            "https://i.ytimg.com/vi/ishbTyLs6ps/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/v/0zM3nApSvMg?fs=1&hl=en_US&rel=0", "maxres"),
            "https://i.ytimg.com/vi/0zM3nApSvMg/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/watch?v=0zM3nApSvMg&feature=feedrec_grec_index", "maxres"),
            "https://i.ytimg.com/vi/0zM3nApSvMg/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/watch?v=0zM3nApSvMg#t=0m10s", "maxres"),
            "https://i.ytimg.com/vi/0zM3nApSvMg/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/embed/dQw4w9WgXcQ", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/v/dQw4w9WgXcQ", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/e/dQw4w9WgXcQ", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/?v=dQw4w9WgXcQ", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/watch?feature=player_embedded&v=dQw4w9WgXcQ", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/?feature=player_embedded&v=dQw4w9WgXcQ", "maxres"),
            "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/user/IngridMichaelsonVEVO#p/u/11/KdwsulMb8EQ", "maxres"),
            "https://i.ytimg.com/vi/KdwsulMb8EQ/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube-nocookie.com/v/6L3ZvIMwZFM?version=3&hl=en_US&rel=0", "maxres"),
            "https://i.ytimg.com/vi/6L3ZvIMwZFM/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/user/dreamtheater#p/u/1/oTJRivZTMLs", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("https://youtu.be/oTJRivZTMLs?list=PLToa5JuFMsXTNkrLJbRlB--76IAOjRM9b", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/watch?v=oTJRivZTMLs&feature=youtu.be", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtu.be/oTJRivZTMLs&feature=channel", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/ytscreeningroom?v=oTJRivZTMLs", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://www.youtube.com/embed/oTJRivZTMLs?rel=0", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/v/oTJRivZTMLs&feature=channel", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/vi/oTJRivZTMLs&feature=channel", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/?v=oTJRivZTMLs&feature=channel", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/?feature=channel&v=oTJRivZTMLs", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/?vi=oTJRivZTMLs&feature=channel", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/watch?v=oTJRivZTMLs&feature=channel", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )
        self.assertEqual(
            YT2TVDB.get_thumbnail_url("http://youtube.com/watch?vi=oTJRivZTMLs&feature=channel", "maxres"),
            "https://i.ytimg.com/vi/oTJRivZTMLs/maxresdefault.jpg"
        )


if __name__ == '__main__':
    unittest.main()
