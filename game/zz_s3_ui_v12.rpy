init 1011 python:
    import re as _s3_v12_re
    _s3_v12_prompts = {'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.': '确定返回主菜单吗？\n未保存的进度将会丢失。', 'Loading will lose unsaved progress.\nAre you sure you want to do this?': '读取存档会丢失未保存的进度。\n确定继续吗？', 'Do you want to load this save?': '要读取这个存档吗？', 'Are you sure you want to quit?': '确定退出游戏吗？', 'Are you sure you want to delete this save?': '确定删除这个存档吗？', 'Are you sure you want to overwrite your save?': '确定覆盖这个存档吗？', 'Get ready!': '准备好！', 'Riding the Waves': '乘风破浪', 'Vixens': '妖娆佳人', 'Calm Before the Snow': '暴雪前的宁静', 'Paradigm Shift': '天翻地覆', 'Smoke and Fire': '烟与火', 'Are you sure you want to return to the main menu?\n\nThis will lose unsaved progress.': '确定返回主菜单吗？\n未保存的进度将会丢失。', 'Are you sure you want to return to the main menu? This will lose unsaved progress.': '确定返回主菜单吗？\n未保存的进度将会丢失。', 'Loading will lose unsaved progress.\n\nAre you sure you want to do this?': '读取存档会丢失未保存的进度。\n确定继续吗？', 'Loading will lose unsaved progress. Are you sure you want to do this?': '读取存档会丢失未保存的进度。\n确定继续吗？'}
    _s3_v12_normalized = {_s3_v12_re.sub(r"\s+", " ", k).strip():v for k,v in _s3_v12_prompts.items()}
    def _s3_v12_prompt(s):
        return _s3_v12_normalized.get(_s3_v12_re.sub(r"\s+", " ", s).strip(), s)
    _s3_v12_previous = config.replace_text
    def _s3_v12_replace(s):
        translated = _s3_v12_prompt(s)
        if translated != s:
            return translated
        return _s3_v12_previous(s) if _s3_v12_previous is not None else s
    config.replace_text = _s3_v12_replace

    # Native display overlays: original artwork is referenced, never modified.
    _s3_v12_scale = persistent.scale_factor
    def _s3_v12_panel(text, x, y, w, h, size=36):
        return (int(x*_s3_v12_scale),int(y*_s3_v12_scale)), Fixed(
            Solid("#111820", xysize=(int(w*_s3_v12_scale),int(h*_s3_v12_scale))),
            Text(text,font="fonts/s3_cn.ttf",size=int(size*_s3_v12_scale),color="#ffffff",xpos=int(22*_s3_v12_scale),ypos=int(20*_s3_v12_scale),xmaximum=int((w-44)*_s3_v12_scale)),
            xysize=(int(w*_s3_v12_scale),int(h*_s3_v12_scale)))
    def _s3_v12_overlay(image_name, panels):
        original = renpy.get_registered_image(image_name)
        if original is None:
            renpy.log("S3CN v1.2: missing image registration " + image_name)
            return
        args=[(int(1920*_s3_v12_scale),int(1080*_s3_v12_scale)),(0,0),original]
        for panel in panels:
            pos, displayable = _s3_v12_panel(*panel)
            args.extend([pos, displayable])
        renpy.image(image_name, Composite(*args))
    _s3_v12_overlay("notebook_tutorial_screen_button",[("点击左上角，打开佐伊的笔记本。",200,15,620,210,40)])
    _s3_v12_overlay("zoey_drawing_tutorial",[
        ("绘画教程\n\n点击蓝色圆点作画，避开红色圆球。\n完成得越快，得分越高。",25,570,820,360,38),
        ("蓝色圆点：点击\n\n红色圆球：避开\n\n点击任意位置开始",980,560,800,380,42)])
    # Log asset names for completing ALL notebook pages, not just screenshots.
    renpy.log("S3CN v1.2 TEST: native UI and tutorial overlays loaded")
    for _s3_v12_file in renpy.list_files():
        if any(k in _s3_v12_file.lower() for k in ("notebook", "zn_page", "zn2_page", "tutorial", "drw_rank")):
            renpy.log("S3CN_ASSET: " + _s3_v12_file)
    for _s3_v12_image in renpy.list_images():
        if any(k in _s3_v12_image.lower() for k in ("zn_page", "zn2_page", "notebook", "drw_rank")):
            renpy.log("S3CN_IMAGE: " + _s3_v12_image + " " + repr(renpy.get_registered_image(_s3_v12_image)))
