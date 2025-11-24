import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        x = tmr % 3200

        # 背景スクロール
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])

        # ---- ここから移動処理 ----
        key = pg.key.get_pressed()

        # 背景スクロール速度（＝こうかとんが押されて左に流れる力）
        scroll_speed = -1

        x, y = scroll_speed, 0   # ←基本は背景と同じ速度で左へ流される

        # 上下キーによる移動（背景に押されつつ上下する）
        if key[pg.K_UP]:
            y = -1
        if key[pg.K_DOWN]:
            y = 1

        # 右キーを押したとき → 右へ動く（背景の流れを打ち消す）
        if key[pg.K_RIGHT]:
            x = 2   # 背景の-1を打ち消して右方向へ移動

        kk_rct.move_ip(x, y)
        # ---------------------

        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
