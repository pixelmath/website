template = '''
<body><meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
<meta content="width=device-width, initial-scale=1" name="viewport" />
<style type="text/css">
img { max-width: 600px; outline: none; text-decoration: none; -ms-interpolation-mode: bicubic;}
    a img { border: none; }
    table { border-collapse: collapse !important;}
    #outlook a { padding:0; }
    .ReadMsgBody { width: 100%; }
    .ExternalClass { width: 100%; }
    .backgroundTable { margin: 0 auto; padding: 0; width: 100% !important; }
    table td { border-collapse: collapse; }
    .ExternalClass * { line-height: 115%; }
    .container-for-gmail-android { min-width: 600px; }


    * {
      font-family: Helvetica, Arial, sans-serif;
    }

    body {
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: none;
      width: 100% !important;
      margin: 0 !important;
      height: 100%;
      color: #607d8b;
    }

    td {
      font-family: Helvetica, Arial, sans-serif;
      font-size: 14px;
      color: #607d8b;
      text-align: center;
      line-height: 21px;
    }

    .pull-left {
      text-align: left;
    }

    .pull-right {
      text-align: right;
    }

    .header-lg,
    .header-md,
    .header-sm {
      font-size: 32px;
      font-weight: 700;
      line-height: normal;
      padding: 35px 0 0;
      color: #36373a;
    }

    .header-md {
      font-size: 24px;
    }

    .header-sm {
      text-align: left;
      padding: 5px 0;
      font-size: 18px;
      line-height: 1.3;
      font-weight: normal !important;
    }

    .content-padding {
      padding: 20px 0 5px;
    }

    .mobile-header-padding-right {
      width: 290px;
      text-align: right;
      padding-left: 10px;
    }

    .mobile-header-padding-left {
      width: 290px;
      text-align: left;
      padding-left: 10px;
      padding: 10px;
    }

    .free-text {
      text-align: left;
      width: 100% !important;
      padding: 10px 60px 0px;
      font-weight: normal !important;
    }

    .button {
      padding: 30px 0;
    }


    .mini-block {
      border: 1px solid #e5e5e5;
      border-radius: 5px;
      background-color: #eaf8fe;
      padding: 12px 15px 15px;
      text-align: left;
      width: 253px;
    }

    .mini-container-left {
      width: 278px;
      padding: 10px 0 10px 15px;
    }

    .mini-container-right {
      width: 278px;
      padding: 10px 14px 10px 15px;
    }

    .product {
      text-align: left;
      vertical-align: top;
      width: 175px;
    }

    .total-space {
      padding-bottom: 8px;
      display: inline-block;
    }

    .item-table {
      padding: 50px 20px;
      width: 560px;
    }

    .item {
      width: 300px;
    }

    .mobile-hide-img {
      text-align: left;
      width: 125px;
    }

    .mobile-hide-img img {
      border: 1px solid #e6e6e6;
      border-radius: 4px;
    }

    .title-dark {
      text-align: left;
      border-bottom: 1px solid #cccccc;
      color: #607d8b;
      font-weight: 700;
      padding-bottom: 5px;
    }

    .item-col {
      padding-top: 20px;
      text-align: left;
      vertical-align: top;
    }

    .force-width-gmail {
      min-width:600px;
      height: 0px !important;
      line-height: 1px !important;
      font-size: 1px !important;
    }

    .btn-green2 {
        color: #fff;
        font-size: 24px;
        min-height: 80px;
        border-radius: 40px;
        text-decoration: none;
        display: inline-block;
        line-height: 24px;
        padding: 24px 40px 25px;
        z-index: 1;
        position: relative;
        border: none;
        background: #5dca88;
        cursor: pointer;
        font-weight: 700;
        text-align: center;
        vertical-align: middle;
        user-select: none;
        transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
    }

    .btn-green2:hover {
        background: #21b191;
        color: white;
        cursor: pointer;
    }

    .footer-copyright {
      font-size:14px;
      font-weight: bold;
      text-align:center;
      padding-bottom: 10px;
    }</style>
<style media="screen" type="text/css">
@import url(http://fonts.googleapis.com/css?family=Oxygen:400,700);</style>
<style media="screen" type="text/css">
@media screen {
      * {
        font-family: 'Oxygen', 'Helvetica Neue', 'Arial', 'sans-serif' !important;
      }
    }</style>
<style media="only screen and (max-width: 480px)" type="text/css">
@media only screen and (max-width: 480px) {

      table[class*="container-for-gmail-android"] {
        min-width: 290px !important;
        width: 100% !important;
      }

      img[class="force-width-gmail"] {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
      }

      table[class="w320"] {
        width: 320px !important;
      }


      td[class*="mobile-header-padding-left"] {
        width: 160px !important;
        padding-left: 0 !important;
      }

      td[class*="mobile-header-padding-right"] {
        width: 160px !important;
        padding-right: 0 !important;
      }

      td[class="header-lg"] {
        font-size: 24px !important;
        padding-bottom: 5px !important;
      }

      td[class="content-padding"] {
        padding: 5px 0 5px !important;
      }

       td[class="button"] {
        padding: 5px 5px 30px !important;
      }

      td[class*="free-text"] {
        padding: 10px 18px 30px !important;
      }

      td[class~="mobile-hide-img"] {
        display: none !important;
        height: 0 !important;
        width: 0 !important;
        line-height: 0 !important;
      }

      td[class~="item"] {
        width: 140px !important;
        vertical-align: top !important;
      }

      td[class~="quantity"] {
        width: 50px !important;
      }

      td[class~="price"] {
        width: 90px !important;
      }

      td[class="item-table"] {
        padding: 30px 20px !important;
      }

      td[class="mini-container-left"],
      td[class="mini-container-right"] {
        padding: 0 15px 15px !important;
        display: block !important;
        width: 290px !important;
      }
    }</style>
<table align="center" cellpadding="0" cellspacing="0" class="container-for-gmail-android" style="padding: 20px;" width="100%">
	<tbody>
		<tr style="border-bottom: 1px solid #e5e5e5">
			<td align="left" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" width="100%">
						<tbody>
							<tr>
								<td height="80" style="text-align: left; vertical-align:middle;" valign="top" width="100%">
									<table cellpadding="0" cellspacing="0" class="w320" width="600">
										<tbody>
											<tr>
												<td class="pull-left mobile-header-padding-left" style="vertical-align: middle;">
													<a href="http://"><img alt="logo" height="100" src="https://pixelmath.org/static/images/logo.png" width="100" /></a><span style="padding-top: 1em; font-size: 3em; top: 0; position: absolute;">PixelMath</span></td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="center" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td>
									<p class="header-md">
										<b>Thank you for registering for the PixelMath Contest on 15th August.</b></p>
									<p class="header-sm" style="text-align: center;">
										We&#39;re really excited to see you participate in India&#39;s first-ever gameful Online Math Contest.</p>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="left" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td class="header-sm">
									<p>
										<b>Just to keep you informed,</b> you will receive the details of the contest at least one week prior to the contest date. You can expect to receive the contest link login credentials and instructions by August 8th. We&#39;ll contact you via the registered email id and phone number.</p>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="left" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td class="header-sm">
									<p>
										<b>While you eagerly await,</b> you can download our PixelMath App and play hundreds of thousands of maths questions aligned to the students&#39; grade.</p>
									<p>
										PixelMath is a math practice app designed to make Math Practice fun using principles of game design, learning sciences and positive psychology.</p>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="left" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td class="header-sm">
									<p>
										PixelMath is available on both Playstore and Appstore.</p>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="left" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td align="center" valign="top" width="50%">
									<a href="https://apps.apple.com/in/app/pixelmath/id1507433163" role="button"><img src="https://pixelmath.org/static/images/app-store-badge.png" style="margin-top: 0;" width="90%" /></a></td>
								<td align="center" valign="middle" width="50%">
									<a href="https://play.google.com/store/apps/details?id=com.rvjeet.pixelmath&hl=en" role="button"><img src="https://pixelmath.org/static/images/google-play-badge.png" width="100%" /></a></td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="left" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td class="header-sm">
									<p>
										You can also <b>follow our <a href="https://www.facebook.com/PixelmathOfficial/" target="_blank">Facebook</a> page</b> where we post exciting math questions to stimulate your mind.</p>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="left" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td class="header-sm">
									<p style="text-align: center;">
										<b>Give your friends a chance to apply to the contest and</b><br />
										<br />
										<strong style="color: rgb(255, 0, 0); font-family: Oxygen, &quot;Helvetica Neue&quot;, Arial, sans-serif;"><span style="background-color:#ffff00;">Win one month FREE subscription of PixelMath&nbsp;</span></strong></p>
									<span style="display: none;">&nbsp;</span>
									<p>
										Click on the share buttons below to forward the contest message on your relevant Whatsapp group and also share&nbsp;it on facebook. Share the screenshot of your post <span style="font-family: Helvetica, Arial, sans-serif;">via whatsapp @8280723657 or&nbsp;</span><span style="font-family: Helvetica, Arial, sans-serif;">via email at&nbsp;</span><span style="font-family: Oxygen, &quot;Helvetica Neue&quot;, Arial, sans-serif;">pixel_updates@pixelmath.org to claim your free subscription.</span></p>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="center" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<a class="share-button-fb" href="https://bit.ly/3ifKQUM" style="padding: 5px;" target="_blank"><img src="https://pixelmath.org/static/images/fb_share.png" /></a><a class="share-button-fb" href="https://bit.ly/3eKdk6T" style="padding: 5px;" target="_blank"><img src="https://pixelmath.org/static/images/whatsapp_share.png" /></a>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr>
			<td align="left" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td class="header-sm">
									<p>
										<b><em>Team PixelMath</em></b></p>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
		<tr style="border-top: 1px solid #e5e5e5">
			<td align="center" class="content-padding" style="background-color: #eaf8fe;" valign="top" width="100%">
				<center>
					<table cellpadding="0" cellspacing="0" class="w320" width="500">
						<tbody>
							<tr>
								<td>
									<p class="footer-copyright">
										Copyright &copy; 2020 PixelMath | Powered by PixelBug Technology Pvt. Ltd.</p>
								</td>
							</tr>
						</tbody>
					</table>
				</center>
			</td>
		</tr>
	</tbody>
</table>
<br />
</body>
'''