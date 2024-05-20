@namespace
class SpriteKind:
    button = SpriteKind.create()

def on_left_pressed():
    animation.run_image_animation(Jogador, assets.animation("""
        myAnim
    """), 200, True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def levelController():
    global Play, cursor, char1, char2
    if level == 0:
        scene.set_background_image(img("""
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999966666699969999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999999999999969999999999999999999999999966999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999999999999999999999996666669
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999969999999999999999999999996669
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999996999
                        9999999999999999999999999999999999999999dd9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999dcb999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999699999
                        999999999999999999999999999999999999999ddcb999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999669999
                        999999999999999999999999999999999999999dbcbb99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999969999999999996999699996
                        999999999999999999999999666999999999999dcccc99999999999699999999999999999999999999999999969999999999999999999999999999999999999999999999999999999999999999996999
                        99999999999999999999999996699999999999dbccccb9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999699999
                        99999999999999999999999996699699999999dbbccbb9999999699999999999999999999999999999999999999999999999999999999999999999969999999999999999969999999999999969999966
                        9999999999999999966999996699999999999ddcbcccbb999996999999999999999996999999999999999999999999999999999999999999999999999999699999999999999999999999699999999969
                        9999999999999999969999999999999999999dbcccccbb999999999999999999999999999699969999999999999999999999999999999999999999999999999999999999999999999669699969999966
                        699969999999999999999999999999666699cdccbcbcccc699999ddddd9969999dbbb9999999699999999999969999999999999999999999999999999999999999999999999696999999969999999996
                        999999999999999999999999999999666696dcbbbcbbbccb99999dbbdb99dd999ddbb9999999999999999999999996999999999999999999999999999969669999999999999999699999969999999999
                        696999999999999999969999999699999996dccccccccccb99969dcccb9ddcc9ddccb6696999999699999999969999999996999999999999999999999666669999999999999999966669696999699999
                        69999699999999999999999999999999669dccccbbbbccccb6966dbcbb9dccc9dbcbb6699999999999999999999999999999999999999999966669966699669999999699999696969996669666669996
                        6999999999999999999969969999999966bdbbbbbbbbbbbbbb966dbccb9dbbb6dbbcc6699999999966999999999999999999996999999669966699669996969999999999996666999996699966666666
                        9999999999999999999999999999999999dbbcccccccccbbbb666dcccbbdccbbccccc6669669669966999966669999999699996999999999966996969996969996999996666666669666666666666666
                        9999999999999999999699999999999999bcccccccccccccbb6666bcbbcccbbccbcbb6666669999666666996969996669999699999999999999999996999699969966699999999666666666666666666
                        999999996699999699999669999999999999cccccccccccc666666bccbcccccccccbb66966666996666669669969966969996999999999999999999999996999669ff6999996996666666666666666ff
                        999999999969999669966699999999999999ccbbbbbbcccc666666cccbbbbbbcccccc66966999996996669999999999999966996969999999966669999996696999f969966666666666666666666ffff
                        999999999999669996966996699999999999bbcbbccbbbbb6666666bbbcbbbccbbbb66666666996669966666999669999966699666999999966966999699669966ff96666669666666666666666fffff
                        999996699696669996999999969999999999bbcbbbbbbbbb66666666bccccccccbb666666666666966966966666669666966696699666999669669666996666666f6666666666666666666666fffffff
                        666996666666699966999999999699999999bbbbcccbbbbb66666666dccccccccc6666666666666666666666666666666666666666666666669666666666666666f666666666666666666666ffffffff
                        666666666666999666696699999966999999bccccccccccb66666666dccbbbbbcc6666666666666666666666666666666666696666666666666666666666666666f66666666666666666666fffffffff
                        6666666666666666666669699969999999999cccccccccc966666666dcbbbccbbc6666666666666666666666666666666666666666666666666666666666666666f666666ff66666666666ffffffffff
                        66666666666666666666b9699999969999b696bcccccccb6f6666666ccbbbbcccc666666666666ff6666666666666666666666666666666666666666666666ff66ff66666ff666666666ffffffffffff
                        666666666666666666dddbbb9dddd699ddb9bb9ccbbbbbfbbddddb666bbccbbbbcbb66666666666f66666666666666666666666666666666666666666666666ff66f666666f66666666fffffffffffff
                        666666666666666666dbbbbfdbbdbbbbbbbb64bccbbbbccdddbbbbbbbcbbbbbbbcc66bbbbbb6666f69666666666666666666666666666666666666666666666fff6ff66666f6f6666fffffffffffffff
                        b6666666b6b6b66666dbbbbfbbbbbbb6bbbb64bbbbbbbccbbcbbcbbcccbbbccbbccbb6b44466666f66666666666666666666666666666f6666666666666666666f66ff6666fff66fffffffffffffffff
                        b6666666b6b6bb66b6dccccbfcccccbbcccb444bbcbccbcbbbbbcbbbccbbbccbbc4bb66bbb444b6666666666666666666666666666666ff6666666666666666666f66f6666ff66ffffffffffffffffff
                        bb6b66bb64bb64bb66dbbbbbbbbbbbbbbcbb444bccbbbccbbcccbbbbccbbbbbbbc44464444bb4b6f66bf6666666666666666666666666ff6666666666666666666ffff6666f66fffffffffffffffffff
                        444466bb44464446b6bccbbbbcbcccbbccbc444bbbbbbcccccccccbbbcbbbbcccc444444bb44bbbfbb6f6666666666666666666666666f666f66666666666666666fff666bffffffffffffffffffffff
                        44b6b4b4b4b6b4444b4bcccccccccccccccc44bcbbbbbcccc4b4cccbbbbcbbcccc4444446644444fbb6f6bbb666666666666666666666f66ff66666666666666666fff6bbfffffffffffffffffffffff
                        444444b4444444444464cbbbbbbcbbbbbbcb444ccbbbbccc44f44ecbbcbbbbbbcc444444b444464f44ffbbbbbb666666666ffff666666f66f6666b666666666666bbff646fffffffffffffffffffffff
                        4444446444444444446bccbccbbccbbbccc4ff4ccbccbcc444ff44ccbcbbbbbbcc4444444444446f44ff46bbbb66666666bfbbfff6666f6f6666666666666666b664ff44ffffffffffffffffffffffff
                        4444b66b4444446664644ccbbbbbbbbccc4ff46ccbbbbcc444444bdbbccbbcbbccff44464444444f44f44466bb4b66b66b6fb4bff6bbbff66666666666666666b444ff4fffffffffffffffffffffffff
                        4444466b44444466644444cccccccccccddddbbccbbbbcc44444dfdbbccbbcbbccffff464464644f44f4b4bbbbbbb666b4ff444fff44ff66bb6666666ff66b6bb4bfffffffffffffffffffffffffffff
                        4444446644444444464464cccccccccccddbbbbccbbbbcc44bb4dfdbbccbbbbbcc44f4664444644fff4444b4b6666666bff646b4ff4ff6b44bb666666f666b44b64fffffffffffffffffffffffffffff
                        4444444444444f44444466ddbbbbbbbbcbbccccccbbbbbcd44ddffdbbccbbbbbcc44444dd44db44fff444444bb6b66664ff44444fffffddbbb444b6b6fb6bbdbdb3ffffffffffffffffffffffffffffc
                        4444464444444f444d4444dbbbccbbbbcbcccccccccbbccd3ddd4ffbbccccccbccddddd4dd3443fff34444bb6bd4d966444444ddffff463d4bd4dd6dff6666dfb4ffffffffffffffffffffffffffffcc
                        4444464444444ff44ff4b4dccbccbbcccbcc44ccbbbbbbccdccccccccccbcbbbccddddd4ddd4ddfffbdddd4dd3ddbddddbd446ddffff444d44bdddddff4669dfddffffffffffffffffffffffffffffcc
                        4444446444444ffddfd344dbcbbbbbcbbbcc4cccbbccbbcbbcccccccccbbbcbcccdd434ddddffdffdddddfddddd3dddddbddddddffff46d444d4ddddffd9dddfdfffffffffffffffffffffffffffffcc
                        44444444444444f3bf44ffdbbbbbcbbbbbbccbbbcbccbbcbbbbcbbbcbbccccccccdddddddddfffffdddddffdddddddddddd444ddffffddddb4ddddddffd66ddfdffffffffffffffffffffffffffffccc
                        44444444ddd444ff4f33ffcbbbbbccbbccbccbbbcbbbbbcbbcccbccccbccbbbbccdddd44ddd4fffdd4dddffd4dddddddddddddddffffddd44b4dddddffdddddffffffffffffffffffffffffffffffccc
                        44444444dddddddfdf44f4bbccbbbbbbccbbbbbbbbbbbbbbbbccbbbcbbbbbbcbccd4ddddddddfffd4dddddffddddddddddddd6bdfffffdd44444dd4ddfdddddffffffffffffffffffffffffffffffccc
                        44444444ddddddd4ff4ff4bbbbbbbcccbbbbbbbbccbbcccbbbbbbbbbcccbbccbccdd4dddddddfffddddddddfddd4ddddddddddddfffffdd44b4ddddddffdddffffffffffffffffffffffffffffffcccc
                        6444444ddd3dd44dff6ff4bbbcbbcccccbbcccbbccbbccbbbcccbbbcccccbccbccddfdddddddfffdddd4dddffdffddddddddddddfffffddddddddddddffddfffffffffffffffffffffffffffffffcccc
                        4344ddddddddd4ddff4fddcbbcbbccbccbbbcbbbbbbbbbbbbcccbccccbccbbbbccdfffddddddfffddddddddffdfdddddddffddddfffffdddddddddddffffffffffffffffffffffffffffffffffffcccc
                        4444ddddb4ddddddfddfd4ccbcbbcccccbbbbbbbbbbbcccbbbbbbcccccccbccbccdffdddddddffffddddddddfffddddd4dffddddfffffddddddddfdfffffffffffffffffffffffffffffffffffffcccc
                        4444deedebd4434efffdd4ccbbbbcccccbbbcccccbccccccbbbbbbbcccccbbbcccdffdddddddffffddddddddfffdddddddfdddddfffffddddfdddfdffffffffffffffffffffffffffffffffffffccccc
                        4444befeebe4d4beff4444ccbcbbcccccbbccbbbbcccbcbccbbbbbbcccccbbccccddfffdddddffffdddddddddffddddddffdddddfffffdddffdddffffffffffffffffffffffffffffffffffffffccccc
                        444eeeefeeeed4e4ff4444ccccbbcccccbbbbbbbccbcbcbcccbccbbcccccbcbbcc44dffdddddffffdddd44dddffddddddffdddddfffffdddffdddfffffffffffffffffffffffffffffffffffffdccccc
                        fffeeffffeeeeeffffeffeccbbbbcccccbbbccbcccbcbcbccccccbbcccccbccbccdddffddddfffffddddd4dddfffdddddffdddddfffffdddffdfffffffffffffffffffffffffffffffffffffffdccccf
                        effeffedeeffffffffffffccbccbcccccbbbbbbcccbcbcbcbccbcbbbccccbccbccdddffddd4fffffdddddddddfffdddbdffd4dddffffffddffffffffffffffffffffffffffffffffffffffffffdccccc
                        beffffedffffffffffffffccbccbbbbbbcccbbccbcbcbcbcbccbbbcbbbbbbbbbbcdddfdddddffffffdddddddbfffdddbcffddddfffffffdfffffffffffffffffffffffffffffffffffffffffffcccccc
                        dfffffffffffffffffffffccbbbbbbbbbccbbbccbcbcbcbcbccbbbccccbbbbbbccdddffdddffffffffdddd4dbffffddddffdddffffffffffffffffffffffffffffffffffffffffffffffffffffcccccc
                        ffffffffffffffffffffffccbbbbbccbbbbbbbccbcbcbcbcbccbbbbbccbbcbbcccffdffdffffffffffffddccdffffdbddffd4fffffffffffffffffffffffffffffffffffffffffffffffffffffbbfccc
                        efffffffffffffffffffffccbcbbcccbbbbbbcccbcbcbcbcbcccbbbbbbbbccbcccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccdbbbbbbbc
                        ffffffffffffffffffffffccbccbccbbbbbcbcccbcbcbcbcbcccbbbbbcccbccbbccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcfcbcbbbbbbb
                        ffffffffffffffffffffffccccbbbbbbbbccccccbcbcbcbcbcccbccbbbccbbcbbcccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcddbbcccbbbccc
                        ffffffffffffffffffffffccccbbbbbcbbcbbcccbcbcbcbcbcccbbbbbbbbbbbbbcccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccbcbbbbccccbbccc
                        fffffffffffffffffffffcccccbbbbbcccbbbcccbcbcbcbcbcccbbbbcccbbbbccccccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbccccbbbbccccbcccc
                        ffffffffffffffffffffffccccbbccbbccbbbcccbcbcbcbcbcccbccbcccbbcccbcccccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccbbcccbbbbbcccbbccc
                        fffffffffffffffffffffbccbbccbbbbbbbbbcccbcbcbcbcbccccccbbbbbbbbbbcccbcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccfccbbbbbccccbbccbbbcc
                        fffffffffffffffffffffbcbbbcbbbbbbbbbbcccbcbcbcbcbcccbcbbbbbbbbbbbccccccbccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccbbcccccbbbbbbccbbccbbccc
                        ffffffffffffffffffffccbbbbbccbcbbbccbcccbcbcbcbcbccccccbbbcccbbbbcccccbbbcfcbcccffffffffffffffffffffffffffffffffffffffffffffffffffffffcdbbcccccbbbbbbcccccbbbccc
                        fffffffffcfffffffffccccccbbccbccbcccbcccbcbcbcbcbcccbcbbbcccbbbbbcccccccbbcccccbcfffcccffffffffffffffffffffffffffffffffffffffffffffffcdcbbbcccbbbbbbbbcccbbbbbcc
                        ddcccffffffffffffcccccbcccbbcbbbbbbbbcccbcbcbcbcbcccbbbbbbbbbbbbbcccccccbbcccccccccccbbcfcffffffffffffffffffffffffffffffffffffffffffcdbbbbbcccbbbbbbccbccccbbbbc
                        bdddfcbffffffffcccccccbbbcccbbbbbbccbcccbcbcbcbcbcccbbbbbbbbbbbccccccccccbcbbcccccccbbbfcbfcffffffffffffffffffffffffffffffffffffffffcdbbbcccccbbbbbbcbcccccbbbbc
                        bbbddbbcffffccccccccccbbcbbcccbbbccbbcccbcbcbcbcbcccbbcbbbbbbbbccccccccccccccccccccccccccbbbbcffffffffffffffffffffffffffffffffffffffcbbbcbccccbbbbbccbccccccbbbc
                        bbbbdbbbbcccccccbccbcccccbbbbbbbbcbcccccbcbcbcbcbcccbbcbbbbbbccccccccccccccccccccccccccccccccccffffffffffffffffffffffffffffffffffffffcbccbccccbbbbccbbcccbbccccc
                        bbbbccccccccccbbbccccccccccccccccccccbbbbbbbbbbbbcccbbcbbbcccccccccbcccccccccccccccccccccccbbcbccbccccfffffffffffffffffffffffffffccffbbcbbcccccbbbccbccccbbbccbc
                        bbbbbbbbccccccbbcccccbcccccccccccccbbcccccccccccbccccbbcbbccccccccccccccbcbcccccccccccccbbbbbbbccccbbbbbfccccccffffffffffffffffcfccccbbbbbbbcccbbccbbccbbbbbbccc
                        bbbccccccbcccccccccbbbbbcccccccccccbbccccccccccccccccccccccccccccccccccccbcccccccccccccbccbbbbbbbccccbcbbbbbbbcccccffffffffcfcccfccccccbcccccccbccbbbbcbbbbbcccb
                        bbccccccbbbbbcccccbbccbbbcccccccbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccbbcccccbccbbbbbbbdbbbcfcccffcbbbbbbccccccbbcccccbbbbbbbccbbbbcccbb
                        ccbddddbbbbbbbcccccbcccccccbccbcbcccccccccccccccbcccccccccbbcccccccccbccccccccccccccccccccbbbccccccbbbcccccccbdbbbbcccccccbbbbbbbbbcccbbbbbbbbbbbbbbccbbbbbbbbbb
                        ddbbbbccbbbbbbbbbbcccbbcccccccccbcccccccccccccccbcccccccccbccccccccccccccccccccccccccccccccccccccbbbbbbbcccccbbbcccccccbccccbbbbbbcccccbbbbbbbbbbbbbbcccbbbbbbbb
                        cbbbbbbbbbbbbbbbbbbcccbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccbccccccccccccccbbbbbbcccccccccbbbbbbbbccbbbbbbccccccccccbbbbbbbbbbcccccbbbbb
                        cbbbccccccccccccbbbbbcbcccccbbccccccccccccbbbbbccccccccccccccccccccccccccccccbbcccbccccccccccccccccbbbbbcccccbbbbbbbbbbbbbbbccccbbbcccccccccccbbbbbbbcccccccbbbb
                        bbbbccccccccbbbbbbbbbbbccbbbbbbbbccccccccbbbcccccbcccccccccccccbbccccccccccccccccccccccccccbcccccccbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbcccccbbbbbccccccccbbcc
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccbbbbbbbccccccccccccbbccccccccccccccccccccccbbbbbbbbbccccbbbccbbbbbbbbbccccccbbbbbbbbbbbbbbbbcbbbbbcccbcc
                        bbbbbbcccccccbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccbcccccccccbbcccbcccccccccccbccccccbcccccccccccbbbbbbbbbbccccccccbbbbbbbbbbbbcccbbccccccbc
                        bbbccbbbccccccccccbbbbbbbccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbcccccbccccbbbbbcccccccbbccccccbbbbbbbbccccccccbccccccbbbbbbbbbbbccbbcccbbbbc
                        bbbcdddddbbbbcccccccccccccbbbbbccccbbcbccccccccccccbcccccccccccccccccccccbcbbbbbbbcccccccccccccccccbbbbbbcccccbbbbbbbbbbcccccccccccccccccccbbbbbbbbbbbbbbbbbbbbb
                        bbbdcbbbbbbbbbbbbbbbbccccbbccccccccccccccccccccccccccccccbbbbbbcccbcccccccccccccbcccccccccccccccccbbbbbbbbcbbbbbbbbcccccccbcccccccccbbccccccccbbbbbbbbbbbbbbbbbb
                        bdbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbccccccccbbbbbbccccccbbbbbbbccccbbbbbbbbbbbbbbbbb
                        cddbccccbbbbbbbbbbbbbbcccccccccccccbbbbbccccccccccbcccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbccccccbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        cdcccbcccbbbbbbbbbbbbbbcccccccbbbbbbcccccccccccccccbbbbbbbbbccccccccccccccccccccccccccccccbbbbbbcccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        dcbbbbbbbbbbbbbbbbbbccccccbbbbbcccccccccccccccccccccccccccccccccccccbbccccccccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        dbbbbbbbbbbbccccccccccccccbbbbcccccccbbccccccccccbccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbcccbbcbbbbbbbbccccccbbccccbbccccccccccccccccccccccccccccccccccbbcccccbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbcccccccccccccccccccccccccccc
                        bbbbbbbccbbbbbbbbbbbbbbbbbbbbcccbbbccccbbbbbbbccccccccccccbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbccccccccccbbbccccccccccccccc
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbccbbbbbbbbbbbbb
                        bbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccbbbbbccccbbbbbbbbbbbbbbbbbbccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbcccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        bbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccc
                        ccccccccccccbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbccccccccbbbbbbbcbbbbbbbbbcccbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccc
                        cccccccccccccccccccccbdddddccccccccccbbbbbbbbbccccccccbbbcccccccccbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbccc
                        cccccccccbbbbbcccccccccccccccccccccbbbbbbbcccccccbbcccccccccccbbbbbbcccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbccccc
                        ccccccccccccbbccccccccccccbbbbbbbbbbbbbccccccbbbbbccccccbbbbbbbbbcbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccc
                        bcccccccccccccccccccccccbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbcccccccbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbcccccccccc
                        bccccccccccccccccbbbbbbbbbbbbbbbbeccccbbdbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccbbbbbbcccccccbbcccccccccccccbbbbb
                        cccccccccccbbbbbbbbbbbbbbbbbbbbbbeeccbbd4bddbbdbbb3b444ddd444bbb344bbddbbcb44bbb44bb3444b444444b4be44ecccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbb
                        bddddcbbbbbbbb444b4bbb44bb4b4bb4444dd44d44ddb4d3bddddddddd444ddddd44ddddddb33dd4444ddd44344444444e4e44ecbceeeccccbcccccccccccccccccccccbbccccccccccccccccbbbbbbb
                        ddbbdd44b44b444444b444b444443444dddddddd4ddddddddddddddd4dddddddbdddddddddddddd44d44dddddd44dddddbd4dd3dd34b3bbdddccccccbbccccccccccccbbbbbbbbbbbbbbcccccbbbbbbb
                        bbeee4b44444444dd4d33ddddddddde4dddddddddddddddddddddddddddddddd4d4ddd4dddddddddddd44ddddddddddddddddddddddd3dddbbbdbbdddbbbbbbcbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                        b4b43dd44db4ddddd4d44dddddddddbd4ddddddddddddddddddddddddd4ddddddd4dddddddddddddddd44ddddddddddddddddddddd4ddddd44dddddddddbdbddddbdbbddddbbbbbbbbbbbbbbbbbccbbb
                        dddd3ddddd4ddddd44dddd4dddddddddddddddddddddddddddddddddddd3dddddd4ddddddddddddddddddddddddddddddddddddddddddddddd4dddddddddddddddddd334db4d3dd4bbd44b3ddbbcbbbb
                        d4dddbddddddddddd4dddd4ddddddddddddddd3dddddddddd444ddddddd4dddddddddddddddddddddddddddddddd4ddddddddddddddddddddd4ddddddddddddddddddddd3bd4ddd4dddd4444444ddddd
                        ddddddddddddddddd4ddddddddddddddddddd4ddddddddddddd4ddddddddddddddddddddddddddddddddddddd4dddddddddddddddddd4ddddddddddd4ddddddddddddddddddd4d44ddddd4dd44dddddd
                        4ddddddd4d444dd4dd4ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd4ddddddddddddddddddddddddddddddd4ddddddddddddddddddddddddddddd4ddddddddd
                        dddddddddd444ddddd3ddddddddddddd4ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd44dddddddddddddddddddddddddddddddddd4ddddddddd
        """))
        game.splash("Bem vindo! Aperte A para", "avançar!")
        Play = sprites.create(img("""
                ....ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff....
                            ...fddddddddddddddddddddddddddddddddddddddddddddddddddddddddddf...
                            ..fdddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbf..
                            .fdddddbbbfffbbbbbffffffbbbbbbffffffbbbbbbffffffbbbbbfffffffbbbbf.
                            fdddddbbbfaaafbbbfaaaaaafbbbbfaaaaaafbbbbfaaaaaafbbbfaaaaaaafbbbbf
                            fddddbbbbfaaafbbfaaaaaaaafbbfaaaaaaaafbbfaaaaaaaafbbfaaaaaaaafbbbf
                            fdddbbbbbfaaafbbfaaaaaaaafbbfaaaffaaafbbfaaaffaaafbbfaaaffaaafbbbf
                            fddbbbbbbfaaafbbfaaaffaaafbbfaaaffffffbbfaaaffaaafbbfaaaffaaafbbbf
                            fdbbbbbbbfaaafbbfaaaffaaafbbfaaaffffffbbfaaaffaaafbbfaaaffaaffbbcf
                            fbbbbbbbbfaaafbbfaaaffaaafbbfaaaffaaafbbfaaaffaaafbbfaaafaaaffbbcf
                            fcbbbbbbbfaaafbcfaaaffaaafbbfaaaffaaafbbfaaaaaaaafbbfaaaaaaaffbbcf
                            fcbbbbbbbfaaafccfaaaffaaafcbfaaafffaafbcfaaaaaaaafcbfaaaaaaaffbccf
                            fccbbfffbfaaafccfaaaffaaafccfaaafffaafccfaaaffaaafccfaaaaaaaafcccf
                            fcccfaaaffaaafccfaaaffaaafccfaaaaaaaafccfaaaffaaafccfaaaffaaafcccf
                            fcccfaaaaaaaafccfaaaaaaaafccfaaaaaaaafccfaaaffaaafccfaaaffaaafcccf
                            fcccffaaaaaaffccffaaaaaaffccffaaaaaaffccfaaaffaaafccfaaaffaaafcccf
                            fcccffffffffffccffffffffffccffffffffffccffffffffffccffffffffffcccf
                            fccccffffffffccccffffffffccccffffffffcccffffffffffccffffffffffcccf
                            .fccccffffffccccccffffffccccccffffffcccccfffccfffccccfffccfffcccf.
                            ..fccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccf..
                            ...fccccccccccccccccccccccccccccccccccccccccccccccccccccccccccf...
                            ....ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff....
            """),
            SpriteKind.button)
        cursor = sprites.create(img("""
                1 1 1 1 1 1 1 1 1 1 1 1 6 
                            . . 1 1 1 1 1 1 1 1 1 6 6 
                            . . . 1 1 1 1 1 1 1 6 6 6 
                            . . . . . 1 1 1 1 6 6 6 6 
                            . . . . . 1 1 1 6 6 6 6 6 
                            . . . . . . 1 6 6 6 6 6 6 
                            . . . . . . 6 6 6 6 6 6 6 
                            . . . . . 6 . . 6 6 6 6 6 
                            . . . . 6 . . . . . 6 6 6 
                            . . . . . . . . . . 6 6 6 
                            . . . . . . . . . . . 6 6 
                            . . . . . . . . . . . . 6 
                            . . . . . . . . . . . . 6
            """),
            SpriteKind.player)
        Play.set_position(76, 80)
        controller.move_sprite(cursor)
        cursor.set_stay_in_screen(True)
    if level == 1:
        sprites.destroy(Play)
        cursor.z = 1
        game.splash("Selecione seu personagem")
        char1 = sprites.create(img("""
                . . . . . . f f f f . . . . . . 
                            . . . . f f f 2 2 f f f . . . . 
                            . . . f f f 2 2 2 2 f f f . . . 
                            . . f f f e e e e e e f f f . . 
                            . . f f e 2 2 2 2 2 2 e e f . . 
                            . . f e 2 f f f f f f 2 e f . . 
                            . . f f f f e e e e f f f f . . 
                            . f f e f b f 4 4 f b f e f f . 
                            . f e e 4 1 f d d f 1 4 e e f . 
                            . . f e e d d d d d d e e f . . 
                            . . . f e e 4 4 4 4 e e f . . . 
                            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                            . . . . . f f f f f f . . . . . 
                            . . . . . f f . . f f . . . . .
            """),
            SpriteKind.button)
        char2 = sprites.create(img("""
                . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 4 5 5 5 5 4 e f . . . 
                            . . f b 3 e 4 4 4 4 e 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 e b 3 e e 3 b e 3 3 f . 
                            . f 3 3 f f e e e e f f 3 3 f . 
                            . f b b f b f e e f b f b b f . 
                            . f b b e 1 f 4 4 f 1 e b b f . 
                            f f b b f 4 4 4 4 4 4 f b b f f 
                            f b b f f f e e e e f f f b b f 
                            . f e e f b d d d d b f e e f . 
                            . . e 4 c d d d d d d c 4 e . . 
                            . . e f b d b d b d b b f e . . 
                            . . . f f 1 d 1 d 1 d f f . . . 
                            . . . . . f f b b f f . . . . .
            """),
            SpriteKind.button)
        char1.set_position(16, 84)
        char2.set_position(114, 84)
    if level == 2:
        scene.set_background_image(img("""
            eeeee2222222222222222222222222222222222ee2222ee2222ee2222222eeeee2222222222222222222222222222222222ee22222eeee222ee2eeeee2222222222222222222222222222222222ee222
                        222eeeee22222222222222222222222222222eee2222eeee2222ee222222222eeeee22222222222222222222222222222eee2222eeeee222ee22222eeeee22222222222222222222222222222eee2222
                        222222eeeeeee222222222222222222222eeee22222eeeeee2222eee2222222222eeeeeee222222222222222222222eeee22222eeee2222ee222222222eeeeeee222222222222222222222eeee22222e
                        222222222eeeeeeeeeeeeee2222222eeeee222222eeee22eee2222eeee22222222222eeeeeeeeeeeeee2222222eeeee222223eeee22222eeee22222222222eeeeeeeeeeeeee2222222eeeee222222eee
                        e222222222222222222222222222eeee2222222eeee22222eef22222eeeee222222222222222222222222222eeee2333333eeee22222efe2eeeee222222222222222222222222222eeee2222222eeee2
                        eeeeeeee22222222222222222222222222222eee2222222eeeefe222222eeeeeeeee22222222222222333333333333322eee2222222efe22222eeeeeeeee22222222222222222222222222222eee2222
                        2222eeeeeeeee222222222222222222222eeee2222222eeeeeeeffe222222222eeeeeeeee222223333333333322222eeee2223322effeee222322222eeeeeeeee222222222222222222222eeee222222
                        2223322222222222222222222222222eeee2222222eeeeeeee222efffe222222222222222222222222222222222eeee2233332efffe22eeeee233333222222222222222222222222222eeee2222222ee
                        2222233332222222222222222222222222222222eeeeeeeee22222eefffe2222222222222222222222222222222233333332efffee22222eeeee2233333333333333333332222222222222222222eeee
                        eeee22233333333333333332222222222222eeeeee222222222eeeee22ffffee22222222223333333333333333333332eeffff22eeeee22222eeeeee23333333333333222222222222222222eeeeeeee
                        eeeeeeeeee233333333332222222222eeeeeee2222222222eeeee2222ffeefffffffee2222222222223333333332fffffffeeff2222eeeee222222eeeeeeee222222222222222222222eeeeeeeeeeeee
                        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee22eeeeeeee2222eee222222ffeeeeeeeeeeffffffffffffffffffffffffeeeeeeeeeeff222222eee2222eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                        eeeeeeeeeee22222222222222ee22222222222222222222222222effeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffe22222222222222222222222222ee22222222222222eeeeeeeeeee
                        eeeeeeeeee22222222222222222eeee2222222222222222222efffeeeeeeeeeeeeeeeeee2eeeeeeeeeeeeeeeeee2eeeeeeeeeeeeeefffe2222222222222222222eeee22222222222222222eeeeeeeeee
                        eeeeeeeeee222222222222222222eeeeeeee222222222eeefffeeeeeeeeeeeeeeeeeeeee222222eeeeeeeeee2222eeeeeeeeeeeeeeeeefffeee222222222eeeeeeee222222222222222222eeeeeeeeee
                        eeeeeeeee2222222222222222222eeeeeeeeeeeeeeeeffffeeeeeeeeeeeeeeeeeeeeeeee22222222222222222222ee2eeeeeeeeeeeeeeeeeffffeeeeeeeeeeeeeeee2222222222222222222eeeeeeeee
                        eeeeeeeee2222222222222222222ee2222effffffffffffeeeeeeeeeeeeeeeeeeeeeeeee22222222222222222222ee22eeeeeeeeeeeeeeeefffffffffffffe2222ee2222222222222222222eeeeeeeee
                        eeeeeeee22e22222222222222222ee2222eeee2efffffffeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeeffffffffe2eeee2222ee22222222222222222e22eeeeeeee
                        eeeeeeee2222222222222222222ee22222ee22eeffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeeffffffffee22ee22222ee2222222222222222222eeeeeeee
                        eeeeeeee2e2222222222222222eee22222ee22efffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeefffffffffe22ee22222eee2222222222222222e2eeeeeeee
                        eeeeeee22e2222222222222222ee222222e22eefffffffeeeeeeeeeeeeeeeeeeeeee22ee22222222222222222222e222eeeeeeeeeeeeeeeefffffffffee22e222222ee2222222222222222e22eeeeeee
                        eeeeeee22e222222222222222ee222222ee22effffffffeeeeeeeeeeeeeeeeee2eee22ee22222222222222222222e222eeee2eeeeeeeeeeeefffffffffe22ee222222ee222222222222222e22eeeeeee
                        eeeeee22e2222222222222222ee222222e22eeffffffffeeeeeeeeeeeeeeeeee2eee22ee22222222222222222222e2222eee2eeeeeeeeeeeefffffffffee22e222222ee2222222222222222e22eeeeee
                        eeeeee22e222222222222222ee222222ee2eeeffffffffeeeeeeeeeeeeeeeeee2ee222e222222222222222222222e2222eee2eeeeeeeeeeeefffffffffe3e2ee222222ee222222222222222e22eeeeee
                        eeeee22ee222222222222222ee22222ee22eefffffffffeeeeeeeeeeeeeeeeee2ee222e2222222222222222222222e222eee2eeeeeeeeeeeeffffffffffe322ee22222ee222222222222222ee22eeeee
                        eeeee22e222222222222222ee222222ee2eeeffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eee2eeeeeeeeeeeeffffffffffe3e2ee222222ee222222222222222e22eeeee
                        eeee22ee222222222222222e222222ee22eefffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eee22eeeeeeeeeeeeffffffffffe322ee222222e222222222222222ee22eeee
                        eeee22ee22e22222222222ee22222ee22eeffffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e222eeee2eeeeeeeeeeeefffffffffff3322ee22222ee22222222222e22ee22eeee
                        eeee2ee222222222222222e222222ee32eeffffffffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeefffffffffffe332ee222222e222222222222222ee2eeee
                        eee22ee22e22222222222e222222ee32eeffffffeffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeffffffffffff3322ee222222e22222222222e22ee22eee
                        eee2ee222e22222222222e22222ee23eeeffffffeffffeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeffffffffffffe3322ee22222e22222222222e222ee2eee
                        ee22ee22e22222222222e222222ee32eefffffffefffeeeeeeeeeeeeeeeeeee22ee222e2222222222222222222222e2222eee2eeeeeeeeeeeeeffffffffffffe332ee222222e22222222222e22ee22ee
                        ee2eee2ee2222222222e222222ee33eeefffffffefffeefeeeeeeeeeeeeeee222ee22ee2222222222222222222222e2222eee22eeeeeeeeeeeeffffffffffffe3322ee222222e2222222222ee2eee2ee
                        eeeee22ee2222222222e22222ee33eeeffffffffffffeefeeeeeeeeeeeeeee22eee22ee2222222222222222222222e2222eee22eeeeeeeeeeeefffffffffffffe3322ee22222e2222222222ee22eeeee
                        eeeee2ee2222222222222222eee33eeffffffffeffffeefeeeeeeeeeeeeeee22eee22ee2222222222222222222222e2222eee22eeeeeeeeeeeefeffffffffffffe332eee2222222222222222ee2eeeee
                        eeee22ee2222222222222222ee33eeeffffffffeffffeefeeeeeeeeeeeeeee22ee222ee2222222222222222222222e2222eee22eeeeeeeeeeeefeffffefffffffe3332ee2222222222222222ee22eeee
                        eeee2ee2222222222222222ee33eeefffffffffeffffeefeeeeeeeeeeeeeee22ee222e22222222222222222222222e2222eee22eeeeeeeeeeeeeeffffeffffffffe3322ee2222222222222222ee2eeee
                        eeee2ee222222222222222ee333eeffffffffffefffeeeeeeeeeeeeeeeeeee22ee222e22222222222222222222222e2222eee22eeeeeeeeeeeeeeefffefffffffffe3322ee222222222222222ee2eeee
                        eee2ee2222222222222222ee33eeeffffffffffefffeeeeeeeeeeeeeeeeeee22ee222e22222222222222222222222e22222ee22eeeeeeeeeeeeeeefffefffffffffee332ee2222222222222222ee2eee
                        eee2ee222222222222222ee33eeefffffffffffefffeefeeeeeeeeeeeeeeee22ee222e22222222222222222222222ee2222eee2eeeeeeeeeeeeeeefffeffffffffffe3332ee222222222222222ee2eee
                        ee2ee2222222222222222e33eeefffffffffffeefffeefeeeeeeeeeeeeeee222ee222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeffffeffffffffffe3322e2322222222222222ee2ee
                        ee2ee222222222222232e333eeffffffffffffeefffeefeeeeeeeeeeeeeee22eee222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffe3322e322222222222222ee2ee
                        e2ee2222222222222322e33eeeffffffffffffeefffeefeeeeeeeeeeeeeee22ee2222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffee332e2322222222222222ee2e
                        e2ee222222222222332e33eeefffffffffffffeefffeefeeeeeeeeeeeeeee22ee2222e22222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffeffffffffffffe3322e322222222222222ee2e
                        eee222222222222332e33eeeffffffffffffffeeffeeeeeeeeeeeeeeeeeee22ee2222222222222222222222222222ee2222eee22eeeeeeeeeeeeeeefffefffffffffffffe3322e322222222222222eee
                        eee222222222222322332eefffffffffffffffefffeefeeeeeeeeeeeeeeee22ee2222222222222222222222222222ee2222eee22eeeeeeeeeeeeeeeeffeefffffffffffffe3322322222222222222eee
                        ee222222222222332333eeeffffffffffffffeefffeefeeeeeeeeeeeeeee222ee22222222222222222222222222222e2222eee22eeeeeeeeeeeeeeeeffeefffffffffffffee3223322222222222222ee
                        ee22222222222332233eeefffffffffffffffeefffeefeeeeeeeeee2eeee222ee22222222222222222222222222222e2222eee22eeeeeeeeeeeeeeeeffeeffffffffffffffee322322222222222222ee
                        e22222222222332233eeeffffffffffffffffeefffeefeeeeeeeeee2eeee22eee22222222222222222222222222222e2222eee22eeeeeeeeeeeeeeeefffefffffffffffffffe3323322222222222222e
                        e22222222222332332eefffffffffffffffffeefffeefeeeeeeeeeeeeeee22eee22222222222222222222222222222e2222eeee2eeeeeeeeeeeeeeeefffeefffffffffffffffe322322222222222222e
                        22222e22222332232eeefffffffffffffffffeefffeefeeeeeeeee2eeeee22ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeeffeefffffffffffffffeee23322222222e22222
                        22222e2222332232eeeffffffffffffffffffeeffeefeeeeeeeeee2eeeee22ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeeffeeffffffffffffffffeee2322222222e22222
                        222222222332222eeeffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeeffeefffffffffffffffffeee332222222222222
                        2222e222233222eeefffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeefffeffffffffffffffffffeee322222222e2222
                        2222e222332222eeefffffffffffffffffffeefffeefeeeeeeeeee2eeee222ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeefffeefffffffffffffffffeee332222222e2222
                        222e222332222eeeffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee222222222222222222222222222222e22222eee22eeeeeeeeeeeeeeeefffeeffffffffffffffffffeee322222222e222
                        222e22232e22eeefffffffffffffffffffffeefffeefeeeeeeeee2eeeee22eee222222222222222222222222222222222222eee22eeeeeeeeeeeeeeeeeffeefffffffffffffffffffee332e22222e222
                        222e22222e2eeeffffffffffffffffffffffeefffefeeeeeeeeee2eeeee22ee2222222222222222222222222222222222222eee22eeeeeeeeeeeeeeeeeffeeffffffffffffffffffffee32e22222e222
                        22ee2222e2eeeffffffffffffffffffffffeeffffefeeeeeeeeee2eeee222ee2222222222222222222222222222222222222eee22eeeeeeeeeeeeeeeeefffefffffffffffffffffffffee32e2222ee22
                        22e22222e2eeeffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee2222222222222222222222222222222222222eee222eeeeeeeeeeeeeeeefffeeffffffffffffffffffffee32e22222e22
                        22e2222eeeeefffffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee2222222222222222222222222222222222222eee222eeeeeeeeeeeeeeeefffeefffffffffffffffffffffeeeee2222e22
                        2ee2222eeeeffffffffffffffffffffffffeefffeefeeeeeeeee22eeee222ee2222222222222222222222222222222222222eeee22e2eeeeeeeeeeeeeefffeeffffffffffffffffffffffeeee2222ee2
                        2e2222eeeefffffffffffffffffffffffffeefffefeeeeeeeeee2eeeee222ee2222222222222222222222222222222222222eeee22eeeeeeeeeeeeeeeeeffeefffffffffffffffffffffffeeee2222e2
                        2e222eee2effffffffffffffffffffffffeeefffefeeeeeeeeee2eeee222eee222e222222222222222222222222222222222eeee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eee222e2
                        2e222eee2effffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee2222e222222222222222222222222222222222eeee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eee222e2
                        ee22eeee2effffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee2222e2222222222222222222222222222e22222eee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe2eeee22ee
                        ee22eee22effffffffffffffffffffffffeeffffefeeeeeeeee22eeee222ee2222e2222222222222222222222222222e22222eee22ee2eeeeeeeeeeeeeefffeeffffffffffffffffffffffe22eee22ee
                        eeeeee22eeffffffffffffffffffffffffeeffffeeeeeeeeeee22eeee222ee2222e2222222222222222222222222222e22222eee22ee2eeeeeeeeeeeeeeeffeeffffffffffffffffffffffee22eeeeee
                        eeeee222efffffffffffffffffffffffffeeffffeeeeeeeeeee2eeeee222ee2222e2222222222222222222222222222e22222eee222e22eeeeeeeeeeeeeefffeeffffffffffffffffffffffe222eeeee
                        2222222eeffffffffffffffffffffffffeeefffeeeeeeeeeee22eeee2222ee2222e2222222222222222222222222222e22222eee222e22eeeeeeeeeeeeeefffeeffffffffffffffffffffffee2222222
                        222222eefffffffffffffffffffffffffeeffffeeeeeeeeeee22eeee2222e22222e2222222222222222222222222222e22222eee222ee2eeeeeeeeeeeeeefffeefffffffffffffffffffffffee222222
                        22222eeefffffffffffffffffffffffffeeffffeeeeeeeeeee22eeee222ee22222e2222222222222222222222222222e22222eeee22ee2eeeeeeeeeeeeeeeffeefffffffffffffffffffffffeee22222
                        222eeeeefffffffffffffffffffffffffeeffffeeeeeeeeeee22eeee222ee22222e2222222222222222222222222222e22222eeee22ee2eeeeeeeeeeeeeeefffeeffffffffffffffffffffffeeeee222
                        eeee2eeeeffffffffffffffffffffffffeeffffeeeeeeeeee22eeeee222ee2222ee2222222222222222222222222222e22222eeee22ee2eeeeeeeeeeeeeeefffeefffffffffffffffffffffeeee2eeee
                        222e2ee2effffffffffffffffffffffffeeffffeeeeeeeeee22eeee2222ee2222ee2222222222222222222222222222e22222eeee22ee22eeeeeeeeeeeeeefffeefffffffffffffffffffffe2ee2e222
                        222e2ee2efffffffffffffffffffffffeeeffffeeeeeeeeee22eeee2222ee2222ee2222222222222222222222222222e22222eeee22ee22eeeeeeeeeeeeeefffeefffffffffffffffffffffe2ee2e222
                        222e2ee2efffffffffffffffffffffffeefffffeeeeeeeeee22eeee2222ee2222ee2222222222222222222222222222e22222eeee222e22eeeeeeeeeeeeeeffffeeffffffffffffffffffffe2ee2e222
                        222e2ee2efffffffffffffffffffffffeefffffeeeeeeeee22eeeee2222ee2222ee2222222222222222222222222222e22222eeee222e22eeeeeeeeeeeeefffffeeffffffffffffffffffffe2ee2e222
                        222e2ee22effffffffffffffffffffffeefffffeeeeeeeee22eeee22222e22222ee2222222222222222222222222222ee2222eeee222ee2eeeeeeeeeeeeeeffffeefffffffffffffffffffe22ee2e222
                        222e2ee22effffffffffffffffffffffeeffffeeeeeeeeee22eeee22222e22222ee2222222222222222222222222222ee2222eeeee22ee2eeeeeeeeeeeeeefffffefffffffffffffffffffe22ee2e222
                        222e2eee2effffffffffffffffffffffeeffffeeeeeeeeee22eeee22222e22222ee2222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeefffffefffffffffffffffffffe2eee2e222
                        222e22ee2eefffffffffffffffffffffefffffeeeeeeeee222eee22222ee22222ee2222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeeffffffffffffffffffffffffee2ee22e222
                        222e22ee22efffffffffffffffffffffefffffeeeeeeeee22eeee22222ee22222ee2222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeeefffffffffffffffffffffffe22ee22e222
                        222e22ee22efffffffffffffffffffffefffffeeeeeeeee22eeee22222ee22222e22222222222222222222222222222ee2222eeeee22ee22eeeeeeeeeeeeeefffffffffffffffffffffffe22ee22e222
                        222e22ee22efffffffffffffffffffffffffffeeeeeeeee22eee222222ee22222e22222222222222222222222222222ee22222eeee222e22eeeeeeeeeeeeeefffffffffffffffffffffffe22ee22e222
                        222e22ee222effffffffffffffffffffffffffeeeeeeeee22eee222222ee22222e22222222222222222222222222222ee22222eeee222ee2eeeeeeeeeeeeeeefffffffffffffffffffffe222ee22e222
                        222e22eee22effffffffffffffffffffffffffeeeeeeee22eeee222222e222222e22222222222222222222222222222ee22222eeee222ee22eeeeeeeeeeeeeefffffffffffffffffffffe22eee22e222
                        222e222ee22effffffffffffffffffffffffffeeeeeeee22eeee222222e222222e22222222222222222222222222222ee22222eeee222ee22eeeeeeeeeeeefffffffffffffffffffffffe22ee222e222
                        222e222ee22eeffffffffffffffffffffffffeeeeeeeee22eee2222222e222222ee22222eeee222eeee222eeee22222ee222222eeee22222eeeeeeeeeeeeeffffffffffffffffffffffee22ee222e222
                        222e222ee222efffffffbffffffffbbbfffffbbeeeeebeeeeeeee222eebeeeeeeddeeeeeeedeeeeeeeeeeeedeeeeeeeddeeeeeebeee22eeeeeeeebeeeeebbfffffbbbffffffffbfffffe222ee222e222
                        222e222ee222ebbfffbbbbbfffffbbbbbbbbbbbbbbbbbbeebbbbeeeeedddeeeedddddeeeddddeeeeddeeeeddddeeedddddeeeedbbbbeeebbbbeebbbbbbbbbbbbbbbbbbfffffbbbbbfffe222ee222e222
                        222ee22ee222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee222ee22ee222
                        222ee22ee2222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2222ee22ee222
                        2222e222e2222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee2222e222e2222
                        2222e222ee2222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2222ee222e2222
                        2222e222ee2222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2222ee222e2222
                        2222e222ee2222eebbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbee2222ee222e2222
                        2222e2222e22e22ebbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbe22e22e2222e2222
                        222222222e22e22eebbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbee22e22e222222222
                        222222222e22e222ebbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbe222e22e222222222
                        2222222222e22e22eebbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbee22e22e2222222222
                        222222e222e22e222ebbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbe222e22e222e222222
                        222222e222222e222eebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbee222e222222e222222
                        222222e2222222e222ebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbe222e2222222e222222
                        222222ee222222e222eebbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbee222e222222ee222222
                        2222222e222222e2222ebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbe2222e222222e2222222
                        22222e2e2222222e222eebbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbee222e2222222e2e22222
                        22222e2e2222222e222eebbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbee222e2222222e2e22222
                        22222e2e22222222e22ebbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbe22e22222222e2e22222
                        22222e2ee2222222e22ebbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbe22e2222222ee2e22222
                        22222e2ee2222222eeeebbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbeeee2222222ee2e22222
                        22222e22e2222222eeebbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbeee2222222e22e22222
                        22222ee2e2222222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee2222222e2ee22222
                        22222ee2e222222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee222222e2ee22222
                        222222e2ee22222ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe22222ee2e222222
                        222222e22e2222eebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbee2222e22e222222
                        222222e22e22eeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeee22e22e222222
                        222222e2eeeeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeee2e222222
                        222222e2ebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbe2e222222
                        222222eeebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeee222222
        """))
        sprites.destroy(cursor)
        sprites.destroy(char1)
        sprites.destroy(char2)
        Jogador.set_position(80, 90)
        Jogador.say_text("Press A to start", 2000, True)
    if level == 3:
        tiles.set_current_tilemap(tilemap("""
            MAPA 2
        """))

def on_on_overlap(sprite, otherSprite):
    global level, Jogador
    if otherSprite == Play and controller.A.is_pressed():
        level = 1
        levelController()
    if otherSprite == char1 and controller.A.is_pressed():
        Jogador = sprites.create(img("""
                . . . . . . f f f f . . . . . . 
                            . . . . f f f 2 2 f f f . . . . 
                            . . . f f f 2 2 2 2 f f f . . . 
                            . . f f f e e e e e e f f f . . 
                            . . f f e 2 2 2 2 2 2 e e f . . 
                            . . f e 2 f f f f f f 2 e f . . 
                            . . f f f f e e e e f f f f . . 
                            . f f e f b f 4 4 f b f e f f . 
                            . f e e 4 1 f d d f 1 4 e e f . 
                            . . f e e d d d d d d e e f . . 
                            . . . f e e 4 4 4 4 e e f . . . 
                            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                            . . . . . f f f f f f . . . . . 
                            . . . . . f f . . f f . . . . .
            """),
            SpriteKind.player)
        level = 2
        levelController()
    if otherSprite == char2 and controller.A.is_pressed():
        Jogador = sprites.create(img("""
                . . . . . f f 4 4 f f . . . . . 
                            . . . . f 5 4 5 5 4 5 f . . . . 
                            . . . f e 4 5 5 5 5 4 e f . . . 
                            . . f b 3 e 4 4 4 4 e 3 b f . . 
                            . . f 3 3 3 3 3 3 3 3 3 3 f . . 
                            . f 3 3 e b 3 e e 3 b e 3 3 f . 
                            . f 3 3 f f e e e e f f 3 3 f . 
                            . f b b f b f e e f b f b b f . 
                            . f b b e 1 f 4 4 f 1 e b b f . 
                            f f b b f 4 4 4 4 4 4 f b b f f 
                            f b b f f f e e e e f f f b b f 
                            . f e e f b d d d d b f e e f . 
                            . . e 4 c d d d d d d c 4 e . . 
                            . . e f b d b d b d b b f e . . 
                            . . . f f 1 d 1 d 1 d f f . . . 
                            . . . . . f f b b f f . . . . .
            """),
            SpriteKind.player)
        level = 2
        animation.run_image_animation(Jogador,
            assets.animation("""
                Knight_idle
            """),
            500,
            True)
        levelController()
    if otherSprite == Jogador and controller.A.is_pressed():
        level = 3
        levelController()
sprites.on_overlap(SpriteKind.player, SpriteKind.button, on_on_overlap)

char2: Sprite = None
char1: Sprite = None
cursor: Sprite = None
Play: Sprite = None
Jogador: Sprite = None
level = 0
level = 0
levelController()
scene.camera_follow_sprite(Jogador)