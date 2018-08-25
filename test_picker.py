#!/usr/bin/env python3

import unittest
import picker

CONTENT = """
<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="ua-linux ua-webkit">
<head>
    <title>
    上饶 - 在线购票&amp;影讯
</title>
</head>

<body>
    <div id="dale_movie_nowplaying_top_left"></div>

    <div id="nowplaying">
        <div class="mod-hd">
            <h2>正在上映</h2>
        </div>
        <div class="mod-bd">
            <ul class="lists">
                    <li
                        id="26636712"
                        class="list-item"
                        data-title="蚁人2：黄蜂女现身"
                        data-score="7.6"
                        data-star="40"
                        data-release="2018"
                        data-duration="119分钟(中国大陆)"
                        data-region="美国"
                        data-director="佩顿·里德"
                        data-actors="保罗·路德 / 伊万杰琳·莉莉 / 迈克尔·佩纳"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="34361"
                        data-subject="26636712"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/26636712/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529389608.webp" alt="蚁人2：黄蜂女现身" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/26636712/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="蚁人2：黄蜂女现身"
                                    data-psource="title">
                                    蚁人2：黄蜂女...
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar40"></span>
                                        <span class="subject-rate">7.6</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F343208%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="27201353"
                        class="list-item"
                        data-title="大师兄"
                        data-score="5.4"
                        data-star="30"
                        data-release="2018"
                        data-duration="100分钟"
                        data-region="中国大陆 香港"
                        data-director="阚家伟"
                        data-actors="甄子丹 / 陈乔恩 / 喻亢"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="1599"
                        data-subject="27201353"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/27201353/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2528842218.webp" alt="大师兄" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/27201353/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="大师兄"
                                    data-psource="title">
                                    大师兄
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar30"></span>
                                        <span class="subject-rate">5.4</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1218190%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30122633"
                        class="list-item"
                        data-title="快把我哥带走"
                        data-score="7.0"
                        data-star="35"
                        data-release="2018"
                        data-duration="115分钟"
                        data-region="中国大陆"
                        data-director="郑芬芬"
                        data-actors="张子枫 / 彭昱畅 / 赵今麦"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="42735"
                        data-subject="30122633"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/30122633/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2531080870.webp" alt="快把我哥带走" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/30122633/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="快把我哥带走"
                                    data-psource="title">
                                    快把我哥带走
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar35"></span>
                                        <span class="subject-rate">7.0</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1216446%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26426194"
                        class="list-item"
                        data-title="巨齿鲨"
                        data-score="6.0"
                        data-star="30"
                        data-release="2018"
                        data-duration="115分钟(中国大陆)"
                        data-region="美国 中国大陆 香港"
                        data-director="乔·德特杜巴"
                        data-actors="杰森·斯坦森 / 李冰冰 / 雷恩·威尔森"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="57639"
                        data-subject="26426194"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/26426194/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530572643.webp" alt="巨齿鲨" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/26426194/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="巨齿鲨"
                                    data-psource="title">
                                    巨齿鲨
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar30"></span>
                                        <span class="subject-rate">6.0</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F346178%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26985127"
                        class="list-item"
                        data-title="一出好戏"
                        data-score="7.3"
                        data-star="40"
                        data-release="2018"
                        data-duration="134分钟"
                        data-region="中国大陆"
                        data-director="黄渤"
                        data-actors="黄渤 / 舒淇 / 王宝强"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="240245"
                        data-subject="26985127"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/26985127/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2529571873.webp" alt="一出好戏" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/26985127/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="一出好戏"
                                    data-psource="title">
                                    一出好戏
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar40"></span>
                                        <span class="subject-rate">7.3</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1203084%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26630714"
                        class="list-item"
                        data-title="精灵旅社3：疯狂假期"
                        data-score="7.0"
                        data-star="35"
                        data-release="2018"
                        data-duration="98分钟"
                        data-region="美国"
                        data-director="格恩迪·塔塔科夫斯基"
                        data-actors="亚当·桑德勒 / 凯瑟琳·哈恩 / 史蒂夫·布西密"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="22382"
                        data-subject="26630714"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/26630714/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530591543.webp" alt="精灵旅社3：疯狂假期" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/26630714/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="精灵旅社3：疯狂假期"
                                    data-psource="title">
                                    精灵旅社3：疯...
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar35"></span>
                                        <span class="subject-rate">7.0</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F343070%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26615753"
                        class="list-item"
                        data-title="黑子的篮球·终极一战"
                        data-score="6.5"
                        data-star="35"
                        data-release="2017"
                        data-duration="91分钟"
                        data-region="日本"
                        data-director="多田俊介"
                        data-actors="小野贤章 / 小野友树 / 神谷浩史"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="2795"
                        data-subject="26615753"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/26615753/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2531651342.webp" alt="黑子的篮球·终极一战" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/26615753/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="黑子的篮球·终极一战"
                                    data-psource="title">
                                    黑子的篮球·终...
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar35"></span>
                                        <span class="subject-rate">6.5</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F569712%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30176525"
                        class="list-item"
                        data-title="深海历险记"
                        data-score="0"
                        data-star="00"
                        data-release="2018"
                        data-duration="92分钟"
                        data-region="中国大陆"
                        data-director="Julio Soto Gurpide"
                        data-actors="张璐 / 陈红 / 张云龙"
                        data-category="nowplaying"
                        data-enough="False"
                        data-showed="True"
                        data-votecount="64"
                        data-subject="30176525"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/30176525/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529479778.webp" alt="深海历险记" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/30176525/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="深海历险记"
                                    data-psource="title">
                                    深海历险记
                                </a>
                            </li>


                            <li class="srating">
                                    

                                        <span class="text-tip">暂无评分</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1218299%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="27107604"
                        class="list-item"
                        data-title="天下第一镖局"
                        data-score="0"
                        data-star="00"
                        data-release="2018"
                        data-duration="90分钟"
                        data-region="中国大陆"
                        data-director="陶盟喜"
                        data-actors="樊少皇 / 车永莉 / 释彦能"
                        data-category="nowplaying"
                        data-enough="False"
                        data-showed="True"
                        data-votecount="71"
                        data-subject="27107604"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/27107604/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2526984156.webp" alt="天下第一镖局" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/27107604/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="天下第一镖局"
                                    data-psource="title">
                                    天下第一镖局
                                </a>
                            </li>


                            <li class="srating">
                                    

                                        <span class="text-tip">暂无评分</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1189889%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30244759"
                        class="list-item"
                        data-title="信仰者"
                        data-score="0"
                        data-star="00"
                        data-release="2018"
                        data-duration="104分钟"
                        data-region="中国大陆"
                        data-director="杨虎"
                        data-actors="黄少祺 / 赵毅 / 葛子铭"
                        data-category="nowplaying"
                        data-enough="False"
                        data-showed="True"
                        data-votecount="234"
                        data-subject="30244759"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/30244759/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2530153907.webp" alt="信仰者" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/30244759/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="信仰者"
                                    data-psource="title">
                                    信仰者
                                </a>
                            </li>


                            <li class="srating">
                                    

                                        <span class="text-tip">暂无评分</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1225029%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="27605698"
                        class="list-item"
                        data-title="西虹市首富"
                        data-score="6.7"
                        data-star="35"
                        data-release="2018"
                        data-duration="118分钟"
                        data-region="中国大陆"
                        data-director="闫非 彭大魔"
                        data-actors="沈腾 / 宋芸桦 / 张一鸣"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="298480"
                        data-subject="27605698"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/27605698/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529206747.webp" alt="西虹市首富" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/27605698/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="西虹市首富"
                                    data-psource="title">
                                    西虹市首富
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar35"></span>
                                        <span class="subject-rate">6.7</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1212592%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26351812"
                        class="list-item"
                        data-title="欧洲攻略"
                        data-score="3.7"
                        data-star="20"
                        data-release="2018"
                        data-duration="100分钟"
                        data-region="中国大陆 英国"
                        data-director="马楚成"
                        data-actors="梁朝伟 / 吴亦凡 / 唐嫣"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="29693"
                        data-subject="26351812"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/26351812/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529410377.webp" alt="欧洲攻略" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/26351812/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="欧洲攻略"
                                    data-psource="title">
                                    欧洲攻略
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar20"></span>
                                        <span class="subject-rate">3.7</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F248162%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30237381"
                        class="list-item"
                        data-title="惊慌失色之诡寓"
                        data-score="0"
                        data-star="00"
                        data-release="2018"
                        data-duration="86分钟"
                        data-region="中国大陆"
                        data-director="齐迹"
                        data-actors="梁辰羽 / 樱雪 / 代佳夕"
                        data-category="nowplaying"
                        data-enough="False"
                        data-showed="True"
                        data-votecount="36"
                        data-subject="30237381"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/30237381/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2531298193.webp" alt="惊慌失色之诡寓" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/30237381/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="惊慌失色之诡寓"
                                    data-psource="title">
                                    惊慌失色之诡寓...
                                </a>
                            </li>


                            <li class="srating">
                                    

                                        <span class="text-tip">暂无评分</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1222188%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26309969"
                        class="list-item"
                        data-title="新乌龙院之笑闹江湖"
                        data-score="3.6"
                        data-star="20"
                        data-release="2018"
                        data-duration="103分钟"
                        data-region="中国大陆"
                        data-director="朱延平"
                        data-actors="王宁 / 孔连顺 / 王智"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="3849"
                        data-subject="26309969"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/26309969/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2529762680.webp" alt="新乌龙院之笑闹江湖" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/26309969/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="新乌龙院之笑闹江湖"
                                    data-psource="title">
                                    新乌龙院之笑闹...
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar20"></span>
                                        <span class="subject-rate">3.6</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F248907%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26906870"
                        class="list-item"
                        data-title="奇怪的袜子精灵"
                        data-score="6.7"
                        data-star="35"
                        data-release="2016"
                        data-duration="86分钟"
                        data-region="捷克 斯洛伐克 克罗地亚"
                        data-director="加林娜·米克林诺瓦"
                        data-actors="克里斯托弗·哈德克 / Jan Maxián / David Novotný"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="121"
                        data-subject="26906870"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/26906870/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2529590610.webp" alt="奇怪的袜子精灵" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/26906870/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="奇怪的袜子精灵"
                                    data-psource="title">
                                    奇怪的袜子精灵...
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar35"></span>
                                        <span class="subject-rate">6.7</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F892394%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="27180974"
                        class="list-item hidden"
                        data-title="浴血广昌"
                        data-score="5.9"
                        data-star="30"
                        data-release="2018"
                        data-duration="100分钟"
                        data-region="中国大陆"
                        data-director="高峰 张馨"
                        data-actors="卢秋宏 / 何达 / 郑昊"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="695"
                        data-subject="27180974"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/27180974/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529260597.webp" alt="浴血广昌" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/27180974/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="浴血广昌"
                                    data-psource="title">
                                    浴血广昌
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar30"></span>
                                        <span class="subject-rate">5.9</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1223430%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30208005"
                        class="list-item hidden"
                        data-title="神秘世界历险记4"
                        data-score="5.4"
                        data-star="30"
                        data-release="2018"
                        data-duration="85分钟"
                        data-region="中国大陆"
                        data-director="王云飞 张林旭 李佳怡"
                        data-actors="阎么么 / 赵一博 / 张磊"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="897"
                        data-subject="30208005"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/30208005/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2528380655.webp" alt="神秘世界历险记4" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/30208005/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="神秘世界历险记4"
                                    data-psource="title">
                                    神秘世界历险记...
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar30"></span>
                                        <span class="subject-rate">5.4</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1220736%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="24852545"
                        class="list-item hidden"
                        data-title="爱情公寓"
                        data-score="2.8"
                        data-star="15"
                        data-release="2018"
                        data-duration="117分钟"
                        data-region="中国大陆"
                        data-director="韦正"
                        data-actors="陈赫 / 袁弘 / 娄艺潇"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="160702"
                        data-subject="24852545"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/24852545/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2521648155.webp" alt="爱情公寓" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/24852545/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="爱情公寓"
                                    data-psource="title">
                                    爱情公寓
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar15"></span>
                                        <span class="subject-rate">2.8</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1175253%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30276726"
                        class="list-item hidden"
                        data-title="爸，我一定行的"
                        data-score="0"
                        data-star="00"
                        data-release="2018"
                        data-duration="100分钟"
                        data-region="中国大陆"
                        data-director="蓝鸿春"
                        data-actors="郑润奇 / 郑鹏生 / 张咏娴"
                        data-category="nowplaying"
                        data-enough="False"
                        data-showed="True"
                        data-votecount="1086"
                        data-subject="30276726"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/30276726/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530908793.webp" alt="爸，我一定行的" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/30276726/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="爸，我一定行的"
                                    data-psource="title">
                                    爸，我一定行的...
                                </a>
                            </li>


                            <li class="srating">
                                    

                                        <span class="text-tip">暂无评分</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1229214%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30236775"
                        class="list-item hidden"
                        data-title="旅行吧！井底之蛙"
                        data-score="0"
                        data-star="00"
                        data-release="2018"
                        data-duration="78分钟"
                        data-region="中国大陆"
                        data-director="陈设"
                        data-actors="王雪沁 / 吴凡 / 周宗禹"
                        data-category="nowplaying"
                        data-enough="False"
                        data-showed="True"
                        data-votecount="130"
                        data-subject="30236775"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/30236775/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530181034.webp" alt="旅行吧！井底之蛙" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/30236775/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="旅行吧！井底之蛙"
                                    data-psource="title">
                                    旅行吧！井底之...
                                </a>
                            </li>


                            <li class="srating">
                                    

                                        <span class="text-tip">暂无评分</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1222190%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="27119292"
                        class="list-item hidden"
                        data-title="大三儿"
                        data-score="7.6"
                        data-star="40"
                        data-release="2018"
                        data-duration="106分钟"
                        data-region="中国大陆"
                        data-director="佟晟嘉"
                        data-actors="叶云"
                        data-category="nowplaying"
                        data-enough="True"
                        data-showed="True"
                        data-votecount="2692"
                        data-subject="27119292"
                    >
                        <ul class="">
                            <li class="poster">
                                <a href="https://movie.douban.com/subject/27119292/?from=playing_poster" class=ticket-btn target="_blank" data-psource="poster">
                                    <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530569532.webp" alt="大三儿" rel="nofollow" class="" />
                                </a>
                            </li>
                            <li class="stitle">
                                <a href="https://movie.douban.com/subject/27119292/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="大三儿"
                                    data-psource="title">
                                    大三儿
                                </a>
                            </li>


                            <li class="srating">
                                        <span class="rating-star allstar40"></span>
                                        <span class="subject-rate">7.6</span>
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1218052%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
            </ul>
        </div>
            <div class="more">显示全部影片</div>
    </div>

    <div id="upcoming">
        <div class="mod-hd">
            <h2>即将上映<a href="/cinema/later/shangrao/" target="_blank">全部&raquo;</a></h2>
        </div>
        <div class="mod-bd">
            <ul class="lists">
                    <li
                        id="27021609"
                        class="list-item"
                        data-title="超大号美人"
                        data-wish="2914"
                        data-duration="110分钟"
                        data-region="美国 中国大陆"
                        data-director="艾比·科恩 马克·西尔弗斯坦"
                        data-actors="艾米·舒默 / 米歇尔·威廉姆斯 / 汤姆·霍珀"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="27021609"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/27021609/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2531291468.webp" alt="超大号美人" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/27021609/?from=playing_poster" target="_blank" title="超大号美人" data-psource="title">
                                        超大号美人
                                    </a>
                            </li>
                            <li class="release-date">
                                08月28日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1204528%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="27077917"
                        class="list-item"
                        data-title="摇滚小子"
                        data-wish="90"
                        data-duration="100分钟"
                        data-region="中国大陆"
                        data-director="段玉宝 王金利"
                        data-actors="安琥 / 徐洁儿 / 苏翊鸣"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="27077917"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/27077917/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2531681767.webp" alt="摇滚小子" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/27077917/?from=playing_poster" target="_blank" title="摇滚小子" data-psource="title">
                                        摇滚小子
                                    </a>
                            </li>
                            <li class="release-date">
                                08月28日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1207515%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30185214"
                        class="list-item"
                        data-title="李学生"
                        data-wish="62"
                        data-duration="100分钟"
                        data-region="中国大陆"
                        data-director="王虎"
                        data-actors="宋禹 / 滕艺 / 董博先"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="30185214"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/30185214/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2531578738.webp" alt="李学生" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/30185214/?from=playing_poster" target="_blank" title="李学生" data-psource="title">
                                        李学生
                                    </a>
                            </li>
                            <li class="release-date">
                                08月28日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1229774%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30238932"
                        class="list-item"
                        data-title="曹操与杨修"
                        data-wish="215"
                        data-duration="121分钟"
                        data-region="中国大陆"
                        data-director="滕俊杰"
                        data-actors="尚长荣 / 言兴朋"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="30238932"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/30238932/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2531189407.webp" alt="曹操与杨修" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/30238932/?from=playing_poster" target="_blank" title="曹操与杨修" data-psource="title">
                                        曹操与杨修
                                    </a>
                            </li>
                            <li class="release-date">
                                08月30日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1224826%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26336252"
                        class="list-item"
                        data-title="碟中谍6：全面瓦解"
                        data-wish="85562"
                        data-duration="148分钟(中国大陆)"
                        data-region="美国"
                        data-director="克里斯托弗·麦奎里"
                        data-actors="汤姆·克鲁斯 / 亨利·卡维尔 / 文·瑞姆斯"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="26336252"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/26336252/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2529365085.webp" alt="碟中谍6：全面瓦解" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/26336252/?from=playing_poster" target="_blank" title="碟中谍6：全面瓦解" data-psource="title">
                                        碟中谍6：全面...
                                    </a>
                            </li>
                            <li class="release-date">
                                08月31日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F341737%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="26728641"
                        class="list-item"
                        data-title="苏丹"
                        data-wish="3614"
                        data-duration="139分钟(中国大陆)"
                        data-region="印度"
                        data-director="阿里·阿巴斯·札法"
                        data-actors="萨尔曼·汗 / 安努舒卡·莎玛 / 马雷塞·克伦普"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="26728641"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/26728641/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2529570494.webp" alt="苏丹" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/26728641/?from=playing_poster" target="_blank" title="苏丹" data-psource="title">
                                        苏丹
                                    </a>
                            </li>
                            <li class="release-date">
                                08月31日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F439495%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30208007"
                        class="list-item"
                        data-title="藏北秘岭-重返无人区"
                        data-wish="993"
                        data-duration="86分钟"
                        data-region="中国大陆"
                        data-director="饶子君"
                        data-actors="蔡宇 / 饶子君 / 土旦巴桑"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="30208007"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/30208007/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2530299035.webp" alt="藏北秘岭-重返无人区" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/30208007/?from=playing_poster" target="_blank" title="藏北秘岭-重返无人区" data-psource="title">
                                        藏北秘岭-重返...
                                    </a>
                            </li>
                            <li class="release-date">
                                08月31日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1220838%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30263334"
                        class="list-item"
                        data-title="解剖室灵异事件之男生宿舍"
                        data-wish="197"
                        data-duration="85分钟"
                        data-region="中国大陆"
                        data-director="战越"
                        data-actors="陈楚洹 / 黄启航 / 龚婉怡"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="30263334"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/30263334/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2531763257.webp" alt="解剖室灵异事件之男生宿舍" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/30263334/?from=playing_poster" target="_blank" title="解剖室灵异事件之男生宿舍" data-psource="title">
                                        解剖室灵异事件...
                                    </a>
                            </li>
                            <li class="release-date">
                                08月31日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1227737%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30238277"
                        class="list-item"
                        data-title="足球王者"
                        data-wish="76"
                        data-duration="90分钟"
                        data-region="中国大陆"
                        data-director="刘骏"
                        data-actors="禹祥 / 绿绮 / 瀚墨"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="30238277"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/30238277/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529790397.webp" alt="足球王者" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/30238277/?from=playing_poster" target="_blank" title="足球王者" data-psource="title">
                                        足球王者
                                    </a>
                            </li>
                            <li class="release-date">
                                08月31日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1208645%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
                    <li
                        id="30227735"
                        class="list-item"
                        data-title="萌宠入殓师"
                        data-wish="70"
                        data-duration="90分钟"
                        data-region="中国大陆"
                        data-director="源唯杰"
                        data-actors="薛明媛 / 傅亨 / 喻言"
                        data-category="upcoming"
                        data-enough="false"
                        data-subject="30227735"
                    >
                        <ul class="">
                            <li class="poster">
                                    <a href="https://movie.douban.com/subject/30227735/?from=playing_poster"
                                        target="_blank"
                                        data-psource="poster">
                                        <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2531220792.webp" alt="萌宠入殓师" rel="nofollow" class="" />
                                    </a>
                            </li>
                            <li class="stitle">
                                    <a class="" href="https://movie.douban.com/subject/30227735/?from=playing_poster" target="_blank" title="萌宠入殓师" data-psource="title">
                                        萌宠入殓师
                                    </a>
                            </li>
                            <li class="release-date">
                                08月31日上映
                            </li>
                                <li class="sbtn">
                                    <a class="ticket-btn"
                                        href="https://movie.douban.com/ticket/redirect/?url=https%3A%2F%2Fm.maoyan.com%2Fcinema%2Fmovie%2F1229217%3F_v_%3Dyes%26merCode%3D1000011"
                                        target="_blank">
                                        选座购票
                                    </a>
                                </li>
                        </ul>
                    </li>
            </ul>
        </div>
    </div>
            </div>
</body>

</html>
"""

class TestPicker(unittest.TestCase):

    def test_get_html(self):
        content = picker.get_html("shanghai")
        assert content is not None

    def test_process(self):
        movies = picker.process(CONTENT)
        assert len(movies) == 21

    def test_gen_table(self):
        movie_list = []
        movie = picker.MovieItem()
        movie.title = "title1"
        movie.score = 6
        movie.votecount = 4000
        movie_list.append(movie)
        movie2 = picker.MovieItem()
        movie2.title = "title2"
        movie2.score = 7
        movie2.votecount = 3000
        movie_list.append(movie2)

        table = picker.gen_table(movie_list, "score")

        assert "title2" in table[0].get_string()
        assert "7" in table[0].get_string()
        assert "3000" in table[0].get_string()

        table = picker.gen_table(movie_list, "vote")
        assert "title1" in table[0].get_string()
        assert "6" in table[0].get_string()
        assert "4000" in table[0].get_string()


if __name__ == '__main__':
    unittest.main()
