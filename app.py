from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from flask import Flask, render_template
import streamlit.components.v1 as components


html_code = """
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous"> -->
    <!--  <link rel="stylesheet" id="picostrap-styles-css" href="https://cdn.livecanvas.com/media/css/library/bundle.css" media="all"> -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/livecanvas-team/ninjabootstrap/dist/css/bootstrap.min.css" media="all">

</head>

<body>


    <div class="container-fluid px-4 py-5 my-5 text-center">
        <div class="lc-block d-block mx-auto mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512" width="5em" height="5em" lc-helper="svg-icon" fill="currentColor">
                <path d="M248 8C111 8 0 119 0 256s111 248 248 248 248-111 248-248S385 8 248 8zm121.8 169.9l-40.7 191.8c-3 13.6-11.1 16.9-22.4 10.5l-62-45.7-29.9 28.8c-3.3 3.3-6.1 6.1-12.5 6.1l4.4-63.1 114.9-103.8c5-4.4-1.1-6.9-7.7-2.5l-142 89.4-61.2-19.1c-13.3-4.2-13.6-13.3 2.8-19.7l239.1-92.2c11.1-4 20.8 2.7 17.2 19.5z"></path>
            </svg>
        </div>
        <div class="lc-block">
            <div editable="rich">

                <h2 class="display-5 fw-bold">The quick brown fox jumps over the lazy dog</h2>

            </div>
        </div>
        <div class="lc-block col-lg-6 mx-auto mb-4">
            <div editable="rich">

                <p class="lead ">Quickly design and customize responsive mobile-first sites with Bootstrap, the world’s most popular front-end open source toolkit, featuring Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful JavaScript plugins.</p>

            </div>
        </div>

        <div class="lc-block d-grid gap-2 d-sm-flex justify-content-sm-center"> <a class="btn btn-primary btn-lg px-4 gap-3" href="#" role="button">Click me, I'm a button</a>
            <a class="btn btn-outline-secondary btn-lg px-4" href="#" role="button">Click me, I'm a button</a>
        </div>
    </div>

    <div class="container" style="padding-top: 10vh;padding-bottom:10vh">
        <div class="row align-items-center px-2">
            <div class="col-12 col-md-7 col-lg-6">
                <div class="lc-block mb-4">
                    <div editable="rich">
                        <h1>The quick brown fox jumps.</h1>
                        <p>Aenean vel nisi in ipsum congue fermentum et ut arcu. Proin leo diam, vulputate eu tellus ac, mattis cursus nunc. Aenean vel nisi in ipsum congue fermentum et ut arcu. Proin leo diam, vulputate eu tellus ac, mattis cursus nunc.</p>
                    </div>
                </div><!-- /lc-block -->
                <div class="lc-block d-flex mb-5">
                    <div class="pe-3">
                        <h3 class="h2 mb-0 text-secondary" editable="inline">100%</h3>
                        <span editable="inline" class="mb-0 text-muted"> Satisfaction </span>
                    </div>
                    <div class="border-start"></div>
                    <div class="px-3">
                        <h3 class="h2 mb-0 text-secondary" editable="inline">24/7</h3>
                        <span editable="inline" class="mb-0 text-muted"> Support </span>
                    </div>
                    <div class="border-start"></div>
                    <div class="ps-3">
                        <h3 class="h2 mb-0 text-secondary" editable="inline">+40k</h3>
                        <span editable="inline" class="mb-0 text-muted"> Products </span>
                    </div>
                </div><!-- /lc-block -->
            </div><!-- /col -->
            <div class="col-12 col-md-5 col-lg-6">
                <div class="lc-block"><img alt="" class="img-fluid mx-auto d-block" src="https://cdn.livecanvas.com/media/svg/undraw-sample/undraw_connected_world_wuay.svg" loading="lazy"></div><!-- /lc-block -->
            </div><!-- /col -->
        </div>
    </div

    <div class="container py-4 py-md-6">
        <div class="row mb-4">
            <div class="col-md-12">
                <div class="lc-block text-center mb-4">
                    <div editable="rich">
                        <h2 class="display-2 fw-bolder">Features&nbsp;</h2>
                    </div>
                </div>
                <div class="lc-block text-center">
                    <div editable="rich">
                        <p class="lead">Lorem ipsum dolor sit amet, consectetur adipiscing elit. <br>Suspendisse a lacus est.&nbsp; </p>
                    </div>
                </div>
                <!-- /lc-block -->
            </div>
            <!-- /col -->
        </div>
        <div class="row">
            <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="lc-block text-center ">
                    <div class="lc-block rounded-circle d-flex justify-content-center align-items-center mx-auto mb-4 bg-light bg-light" style="width:72px;
height:72px;
 ">
                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" fill="currentColor" viewBox="0 0 16 16" style="" lc-helper="svg-icon" class="text-primary">
                            <path fill-rule="evenodd" d="M14 4.5V14a2 2 0 0 1-2 2v-1a1 1 0 0 0 1-1V4.5h-2A1.5 1.5 0 0 1 9.5 3V1H4a1 1 0 0 0-1 1v9H2V2a2 2 0 0 1 2-2h5.5L14 4.5Zm-7.839 9.166v.522c0 .256-.039.47-.117.641a.861.861 0 0 1-.322.387.877.877 0 0 1-.469.126.883.883 0 0 1-.471-.126.868.868 0 0 1-.32-.386 1.55 1.55 0 0 1-.117-.642v-.522c0-.257.04-.471.117-.641a.868.868 0 0 1 .32-.387.868.868 0 0 1 .471-.129c.176 0 .332.043.469.13a.861.861 0 0 1 .322.386c.078.17.117.384.117.641Zm.803.519v-.513c0-.377-.068-.7-.205-.972a1.46 1.46 0 0 0-.589-.63c-.254-.147-.56-.22-.917-.22-.355 0-.662.073-.92.22a1.441 1.441 0 0 0-.589.627c-.136.271-.205.596-.205.975v.513c0 .375.069.7.205.973.137.271.333.48.59.627.257.144.564.216.92.216.357 0 .662-.072.916-.216.256-.147.452-.356.59-.627.136-.274.204-.598.204-.973ZM0 11.926v4h1.459c.402 0 .735-.08.999-.238a1.45 1.45 0 0 0 .595-.689c.13-.3.196-.662.196-1.084 0-.42-.065-.778-.196-1.075a1.426 1.426 0 0 0-.59-.68c-.263-.156-.598-.234-1.004-.234H0Zm.791.645h.563c.248 0 .45.05.609.152a.89.89 0 0 1 .354.454c.079.201.118.452.118.753a2.3 2.3 0 0 1-.068.592 1.141 1.141 0 0 1-.196.422.8.8 0 0 1-.334.252 1.298 1.298 0 0 1-.483.082H.79V12.57Zm7.422.483a1.732 1.732 0 0 0-.103.633v.495c0 .246.034.455.103.627a.834.834 0 0 0 .298.393.845.845 0 0 0 .478.131.868.868 0 0 0 .401-.088.699.699 0 0 0 .273-.248.8.8 0 0 0 .117-.364h.765v.076a1.268 1.268 0 0 1-.226.674c-.137.194-.32.345-.55.454a1.81 1.81 0 0 1-.786.164c-.36 0-.664-.072-.914-.216a1.424 1.424 0 0 1-.571-.627c-.13-.272-.194-.597-.194-.976v-.498c0-.379.066-.705.197-.978.13-.274.321-.485.571-.633.252-.149.556-.223.911-.223.219 0 .421.032.607.097.187.062.35.153.489.272a1.326 1.326 0 0 1 .466.964v.073H9.78a.85.85 0 0 0-.12-.38.7.7 0 0 0-.273-.261.802.802 0 0 0-.398-.097.814.814 0 0 0-.475.138.868.868 0 0 0-.301.398Z"></path>
                        </svg>
                    </div>
                    <div class="lc-block">
                        <div editable="rich">
                            <h5 class="">Lorem ipsum</h5>
                            <p class="text-muted">Take care to develop resources continually and integrity them with previous projects.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="lc-block text-center ">
                    <div class="lc-block rounded-circle d-flex justify-content-center align-items-center mx-auto mb-4 bg-light" style="width:72px;
height:72px;
">
                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" fill="currentColor" class="text-success" viewBox="0 0 16 16" style="" lc-helper="svg-icon">
                            <path d="M11 2a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h1V7a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7h1V2zm1 12h2V2h-2v12zm-3 0V7H7v7h2zm-5 0v-3H2v3h2z"></path>
                        </svg>
                    </div>
                    <div class="lc-block">
                        <div editable="rich">
                            <h5 class="">Lorem ipsum</h5>
                            <p class="text-muted">Take care to develop resources continually and integrity them with previous projects.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="lc-block text-center ">
                    <div class="lc-block rounded-circle d-flex justify-content-center align-items-center mx-auto mb-4 bg-light" style="width:72px;
height:72px;
">
                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" fill="currentColor" class="text-danger" viewBox="0 0 16 16" style="" lc-helper="svg-icon">
                            <path d="M3.05 3.05a7 7 0 0 0 0 9.9.5.5 0 0 1-.707.707 8 8 0 0 1 0-11.314.5.5 0 0 1 .707.707zm2.122 2.122a4 4 0 0 0 0 5.656.5.5 0 1 1-.708.708 5 5 0 0 1 0-7.072.5.5 0 0 1 .708.708zm5.656-.708a.5.5 0 0 1 .708 0 5 5 0 0 1 0 7.072.5.5 0 1 1-.708-.708 4 4 0 0 0 0-5.656.5.5 0 0 1 0-.708zm2.122-2.12a.5.5 0 0 1 .707 0 8 8 0 0 1 0 11.313.5.5 0 0 1-.707-.707 7 7 0 0 0 0-9.9.5.5 0 0 1 0-.707zM6 8a2 2 0 1 1 2.5 1.937V15.5a.5.5 0 0 1-1 0V9.937A2 2 0 0 1 6 8z"></path>
                        </svg>
                    </div>
                    <div class="lc-block">
                        <div editable="rich">
                            <h5 class="">Lorem ipsum</h5>
                            <p class="text-muted">Take care to develop resources continually and integrity them with previous projects.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-6 col-xl-3 mb-4">
                <div class="lc-block text-center ">
                    <div class="lc-block rounded-circle d-flex justify-content-center align-items-center mx-auto mb-4 bg-light" style="width:72px;
height:72px;
">
                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" fill="currentColor" class="text-info" viewBox="0 0 16 16" style="" lc-helper="svg-icon">
                            <path d="M14.082 2.182a.5.5 0 0 1 .103.557L8.528 15.467a.5.5 0 0 1-.917-.007L5.57 10.694.803 8.652a.5.5 0 0 1-.006-.916l12.728-5.657a.5.5 0 0 1 .556.103zM2.25 8.184l3.897 1.67a.5.5 0 0 1 .262.263l1.67 3.897L12.743 3.52 2.25 8.184z"></path>
                        </svg>
                    </div>
                    <div class="lc-block">
                        <div editable="rich">
                            <h5 class="">Lorem ipsum</h5>
                            <p class="text-muted">Take care to develop resources continually and integrity them with previous projects.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>



    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>

</body>

</html>
"""

components.html(html_code,height=2000)


# options = Options()
# options.add_argument("--headless=new")
# options.add_argument('--verbose')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument("--window-size=1920x1080")
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
# driver = webdriver.Chrome(options=options)

# url = st.text_input("podaj adres strony")
# start = st.button('START')
# if start:
#     driver.get(url)
#     driver.quit()


