




<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-xNOnN+2GpZhQXkj5yBrbdwE//RNeJisU3rS/dibnFLGhzI+M0MeGiyt2N1cESfcID9EjasuxUgtU4fpzN1WA+g==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-c4d3a737ed86a598505e48f9c81adb77.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-zUtB2ZWo+zbRCzKWWahQaHp94ByXJWAKDCen4rI/sJCaMAz+uh3G1+K23t4BzajZ7ZYFW6uUgDjDRnT5budaxw==" rel="stylesheet" href="https://github.githubassets.com/assets/github-cd4b41d995a8fb36d10b329659a85068.css" />
    
    
    
    


  <meta name="viewport" content="width=device-width">
  
  <title>python-sc2/onebase_battlecruiser.py at develop · BurnySc2/python-sc2</title>
    <meta name="description" content="A StarCraft II bot api client library for Python 3 - BurnySc2/python-sc2">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">
  <meta name="apple-itunes-app" content="app-id=1477376905">

    <meta name="twitter:image:src" content="https://avatars1.githubusercontent.com/u/21288725?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="BurnySc2/python-sc2" /><meta name="twitter:description" content="A StarCraft II bot api client library for Python 3 - BurnySc2/python-sc2" />
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/21288725?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="BurnySc2/python-sc2" /><meta property="og:url" content="https://github.com/BurnySc2/python-sc2" /><meta property="og:description" content="A StarCraft II bot api client library for Python 3 - BurnySc2/python-sc2" />



  

  <link rel="assets" href="https://github.githubassets.com/">
    <link rel="shared-web-socket" href="wss://alive.github.com/_sockets/u/55979445/ws?session=eyJ2IjoiVjMiLCJ1Ijo1NTk3OTQ0NSwicyI6NTg0MTgzMjI3LCJjIjoxNzE1NjQyMjkwLCJ0IjoxNjAxMjM2NDIwfQ==--4921dc601a87dfedc23e67d8af31d280468f587eb124409c0307e9b2351a8b64" data-refresh-url="/_alive">
  <link rel="sudo-modal" href="/sessions/sudo_modal">

  <meta name="request-id" content="D29D:E4B1:A8FD869:F69B71B:5F70EDC0" data-pjax-transient="true" /><meta name="html-safe-nonce" content="8d8b106b04e6931bbe883e987a8603fba0c67d2f" data-pjax-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9CdXJueVNjMi9weXRob24tc2MyL3RyZWUvZGV2ZWxvcC9leGFtcGxlcy90ZXJyYW4iLCJyZXF1ZXN0X2lkIjoiRDI5RDpFNEIxOkE4RkQ4Njk6RjY5QjcxQjo1RjcwRURDMCIsInZpc2l0b3JfaWQiOiI4MzQ0OTY1NDYwMjEyNDQ2ODI5IiwicmVnaW9uX2VkZ2UiOiJmcmEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-pjax-transient="true" /><meta name="visitor-hmac" content="66126ec494e6bf19530022b6ce94a1c4e2f4fde605b1853e1bb094f6e22bcf76" data-pjax-transient="true" /><meta name="cookie-consent-required" content="false" />

    <meta name="hovercard-subject-tag" content="repository:188820422" data-pjax-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code" data-pjax-transient="true" />

  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-actor-id" content="55979445" /><meta name="octolytics-actor-login" content="8rax" /><meta name="octolytics-actor-hash" content="6ae34b7d5c75ccfa585ac26d55b5f7aa76a87011cca196dfbaaf5b0884e31307" />

  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />

  





    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="460d6cbb141de0559209d936da41283b">

<meta class="js-ga-set" name="dimension10" content="Responsive" data-pjax-transient>

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="8rax">


      <meta name="expected-hostname" content="github.com">

      <meta name="js-proxy-site-detection-payload" content="MDI5Zjg5ZGJiNDMzY2ZiMWI4ZDBiYzJjZTA4ZDM5MmRhMzVkYWRmZmMzNjdhMTJmZDA2MDY5ZTZiZmI3NTc0Nnx7InJlbW90ZV9hZGRyZXNzIjoiMTQ0LjIuMTIwLjE5NiIsInJlcXVlc3RfaWQiOiJEMjlEOkU0QjE6QThGRDg2OTpGNjlCNzFCOjVGNzBFREMwIiwidGltZXN0YW1wIjoxNjAxMjM2NDIwLCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="MARKETPLACE_PENDING_INSTALLATIONS,JS_HTTP_CACHE_HEADERS,PRESERVE_STALE_COMMENTS">

  <meta http-equiv="x-pjax-version" content="459bc655dc92a7098f9f6369c8c2d4a809a2268536ba1cb5d7dcc2ffb97257ef">
  

        <link href="https://github.com/BurnySc2/python-sc2/commits/develop.atom" rel="alternate" title="Recent Commits to python-sc2:develop" type="application/atom+xml">

  <meta name="go-import" content="github.com/BurnySc2/python-sc2 git https://github.com/BurnySc2/python-sc2.git">

  <meta name="octolytics-dimension-user_id" content="21288725" /><meta name="octolytics-dimension-user_login" content="BurnySc2" /><meta name="octolytics-dimension-repository_id" content="188820422" /><meta name="octolytics-dimension-repository_nwo" content="BurnySc2/python-sc2" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="188820422" /><meta name="octolytics-dimension-repository_network_root_nwo" content="BurnySc2/python-sc2" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive page-blob">
    

    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
      <span class="progress-pjax-loader width-full js-pjax-loader-bar Progress position-fixed">
    <span style="background-color: #79b8ff;width: 0%;" class="Progress-item progress-pjax-loader-bar "></span>
</span>      
      



          <header class="Header js-details-container Details px-3 px-md-4 px-lg-5 flex-wrap flex-md-nowrap" role="banner">
    <div class="Header-item mt-n1 mb-n1  d-none d-md-flex">
      <a class="Header-link" href="https://github.com/" data-hotkey="g d"
  aria-label="Homepage " data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>

    </div>

    <div class="Header-item d-md-none">
      <button class="Header-link btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
        <svg height="24" class="octicon octicon-three-bars" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z"></path></svg>
      </button>
    </div>

    <div class="Header-item Header-item--full flex-column flex-md-row width-full flex-order-2 flex-md-order-none mr-0 mr-md-3 mt-3 mt-md-0 Details-content--hidden-not-important d-md-flex">
          <div class="header-search header-search-current js-header-search-current flex-auto js-site-search position-relative flex-self-stretch flex-md-self-auto mb-3 mb-md-0 mr-0 mr-md-3 scoped-search site-scoped-search js-jump-to js-header-search-current-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="188820422" data-scoped-search-url="/BurnySc2/python-sc2/search" data-unscoped-search-url="/search" action="/BurnySc2/python-sc2/search" accept-charset="UTF-8" method="get">
      <label class="form-control input-sm header-search-wrapper p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations"
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" value="Ww/jxhDJ2AWmcmT8+jxPazHcX8ziMvDcxmJaKuuk8Sc+minLJdT0f12LAFp0gaq+OXmQQcVLgDJ+eg58DDLNMg==" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


      <nav class="d-flex flex-column flex-md-row flex-self-stretch flex-md-self-auto" aria-label="Global">
    <a class="Header-link py-md-3 d-block d-md-none py-2 border-top border-md-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
      Dashboard
</a>
    <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade-15" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
        Pull<span class="d-inline d-md-none d-lg-inline"> request</span>s
</a>
    <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade-15" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
      Issues
</a>

    <div class="d-flex position-relative">
      <a class="js-selected-navigation-item Header-link flex-auto mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link mt-md-n3 mb-md-n3 py-2 py-md-3 mr-0 mr-md-3 border-top border-md-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
    Explore
</a>



    <a class="Header-link d-block d-md-none mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade-15" href="/8rax">
      <img class="avatar avatar-user" src="https://avatars1.githubusercontent.com/u/55979445?s=40&amp;v=4" width="20" height="20" alt="@8rax" />
      8rax
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="k7jxZIIxIAU/4V+mJFtqjfotnoExD5lULWyXQhGwZzuPzCfNKKU2LXpmyqFZlv2Fhp5LsylVotu4XgDAkWSjuQ==" />
      <button type="submit" class="Header-link mr-0 mr-md-3 py-2 py-md-3 border-top border-md-top-0 border-white-fade-15 d-md-none btn-link d-block width-full text-left" data-ga-click="Header, sign out, icon:logout" style="padding-left: 2px;">
        <svg class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.75C2 1.784 2.784 1 3.75 1h2.5a.75.75 0 010 1.5h-2.5a.25.25 0 00-.25.25v10.5c0 .138.112.25.25.25h2.5a.75.75 0 010 1.5h-2.5A1.75 1.75 0 012 13.25V2.75zm10.44 4.5H6.75a.75.75 0 000 1.5h5.69l-1.97 1.97a.75.75 0 101.06 1.06l3.25-3.25a.75.75 0 000-1.06l-3.25-3.25a.75.75 0 10-1.06 1.06l1.97 1.97z"></path></svg>
        Sign out
      </button>
</form></nav>

    </div>

    <div class="Header-item Header-item--full flex-justify-center d-md-none position-relative">
      <a class="Header-link" href="https://github.com/" data-hotkey="g d"
  aria-label="Homepage " data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>

    </div>

    <div class="Header-item mr-0 mr-md-3 flex-order-1 flex-md-order-none">
      

    <notification-indicator class="js-socket-channel" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6NTU5Nzk0NDUiLCJ0IjoxNjAxMjM2NDIwfQ==--d76321bd78cc8455eb9de00b91c2ddb5986e0593ff4a8b2bb602e2f8a3206747">
      <a href="/notifications"
         class="Header-link notification-indicator position-relative tooltipped tooltipped-sw"
         
         aria-label="You have no unread notifications"
         data-hotkey="g n"
         data-ga-click="Header, go to notifications, icon:read"
         data-target="notification-indicator.link">
         <span class="mail-status " data-target="notification-indicator.modifier" ></span>
         <svg class="octicon octicon-bell" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path></svg>
      </a>
    </notification-indicator>

    </div>


    <div class="Header-item position-relative d-none d-md-flex">
      <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
      <svg class="octicon octicon-plus" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2a.75.75 0 01.75.75v4.5h4.5a.75.75 0 010 1.5h-4.5v4.5a.75.75 0 01-1.5 0v-4.5h-4.5a.75.75 0 010-1.5h4.5v-4.5A.75.75 0 018 2z"></path></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="BurnySc2/python-sc2">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/BurnySc2/python-sc2/issues/new/choose" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

    </div>

    <div class="Header-item position-relative mr-0 d-none d-md-flex">
      
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/8rax/feature_preview/indicator_check">

  <summary class="Header-link"
    aria-label="View profile and more"
    data-ga-click="Header, show menu, icon:avatar">
    <img
  alt="@8rax"
  width="20"
  height="20"
  src="https://avatars2.githubusercontent.com/u/55979445?s=60&amp;v=4"
  class="avatar avatar-user " />

      <span class="feature-preview-indicator js-feature-preview-indicator" style="top: 10px;" hidden></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw" style="width: 180px" >
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/8rax" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">8rax</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context lh-condensed" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container rounded-1 px-2 py-1 mt-2 border"
  data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit "
      role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:21288725,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:55979445,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;}}" data-hydro-click-hmac="b839bacdb31197d01ccfd91f9c4b4e4d57471efd37d6c8c53b43bda628c81cce">
      <div class="d-flex flex-items-center flex-items-stretch">
        <div class="f6 lh-condensed user-status-header d-flex user-status-emoji-only-header circle">
          <div class="user-status-emoji-container flex-shrink-0 mr-2 d-flex flex-items-center flex-justify-center lh-condensed-ultra v-align-bottom">
            <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM5 8a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zM5.32 9.636a.75.75 0 011.038.175l.007.009c.103.118.22.222.35.31.264.178.683.37 1.285.37.602 0 1.02-.192 1.285-.371.13-.088.247-.192.35-.31l.007-.008a.75.75 0 111.222.87l-.614-.431c.614.43.614.431.613.431v.001l-.001.002-.002.003-.005.007-.014.019a1.984 1.984 0 01-.184.213c-.16.166-.338.316-.53.445-.63.418-1.37.638-2.127.629-.946 0-1.652-.308-2.126-.63a3.32 3.32 0 01-.715-.657l-.014-.02-.005-.006-.002-.003v-.002h-.001l.613-.432-.614.43a.75.75 0 01.183-1.044h.001z"></path></svg>
          </div>
        </div>
        <div class="
          
           user-status-message-wrapper f6 min-width-0"
           style="line-height: 20px;" >
          <div class="css-truncate css-truncate-target width-fit text-gray-dark text-left">
              <span class="text-gray">Set status</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?circle=0&amp;compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="iJEPpfgYwBv/O4k7UmpWTW6ZIKysVWNpjYQk/F/GCwGUAYoVI6Dg6x6VOPsrT8riW7Xc9lSDGbOsrZNnez8NxA==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden></span>
                  <span class="js-user-status-custom-emoji"></span>
                  <span class="js-user-status-no-emoji-icon" >
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM5 8a1 1 0 100-2 1 1 0 000 2zm7-1a1 1 0 11-2 0 1 1 0 012 0zM5.32 9.636a.75.75 0 011.038.175l.007.009c.103.118.22.222.35.31.264.178.683.37 1.285.37.602 0 1.02-.192 1.285-.371.13-.088.247-.192.35-.31l.007-.008a.75.75 0 111.222.87l-.614-.431c.614.43.614.431.613.431v.001l-.001.002-.002.003-.005.007-.014.019a1.984 1.984 0 01-.184.213c-.16.166-.338.316-.53.445-.63.418-1.37.638-2.127.629-.946 0-1.652-.308-2.126-.63a3.32 3.32 0 01-.715-.657l-.014-.02-.005-.006-.002-.003v-.002h-.001l.613-.432-.614.43a.75.75 0 01.183-1.044h.001z"></path></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input
                  type="text"
                  autocomplete="off"
                  data-no-org-url="/autocomplete/user-suggestions"
                  data-org-url="/suggestions?mention_suggester=1"
                  data-maxlength="80"
                  class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field"
                  placeholder="What's happening?"
                  name="message"
                  value=""
                  aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
          <div class="d-inline-block f5 mr-2 pt-3 pb-2" >
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="btn btn-sm v-align-baseline" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2020-09-27T22:23:40+02:00">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2020-09-27T22:53:40+02:00">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2020-09-28T01:53:40+02:00">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2020-09-27T23:59:59+02:00">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2020-09-27T23:59:59+02:00">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit" disabled class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button" disabled class="width-full js-clear-user-status-button btn ml-2 ">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>

    <a role="menuitem" class="dropdown-item" href="/8rax" data-ga-click="Header, go to profile, text:your profile" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;YOUR_PROFILE&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="7a89206e4624183433ddddcb6ffd9d7983973c9d0cda21df6562dfc95a7a8368" >Your profile</a>

    <a role="menuitem" class="dropdown-item" href="/8rax?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;YOUR_REPOSITORIES&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="c3f8752eb6c7c8a15d884005d0cca1ec24f5deba0615bb978a1749bd8f5b63f9" >Your repositories</a>



    <a role="menuitem" class="dropdown-item" href="/8rax?tab=projects" data-ga-click="Header, go to projects, text:your projects" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;YOUR_PROJECTS&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="1953809192ba7243eee7c29572c9a611ad47e382f735d962d9b907cd3e51dd9c" >Your projects</a>


    <a role="menuitem" class="dropdown-item" href="/8rax?tab=stars" data-ga-click="Header, go to starred repos, text:your stars" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;YOUR_STARS&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="1dc8fcce307e4940d328c0ca22a3a059da7e5d85ec1eec176cebff0ed8849efa" >Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;YOUR_GISTS&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="26cbdcb4180c200b640d38751c1ae8f4cf8ff06b03bcdab0645aa2171dc97305" >Your gists</a>





    <div role="none" class="dropdown-divider"></div>
      <a role="menuitem" class="dropdown-item" href="/settings/billing" data-ga-click="Header, go to billing, text:upgrade" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;UPGRADE&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="25cb65091c606491e1260975daf74274edfd393219211e6d52551b54cfe26379" >Upgrade</a>
      
<div id="feature-enrollment-toggle" class="hide-sm hide-md feature-preview-details position-relative">
  <button
    type="button"
    class="dropdown-item btn-link"
    role="menuitem"
    data-feature-preview-trigger-url="/users/8rax/feature_previews"
    data-feature-preview-close-details="{&quot;event_type&quot;:&quot;feature_preview.clicks.close_modal&quot;,&quot;payload&quot;:{&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}"
    data-feature-preview-close-hmac="a5017392117ec48dfb82ad8bbe1725e1ad82ad519422cf1cb9a9d7427c014437"
    data-hydro-click="{&quot;event_type&quot;:&quot;feature_preview.clicks.open_modal&quot;,&quot;payload&quot;:{&quot;link_location&quot;:&quot;user_dropdown&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}"
    data-hydro-click-hmac="18766c7636a6de0c0c97202236db2f8cd9cf83c7734ed0890fd2d984e658e4be"
  >
    Feature preview
  </button>
    <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
</div>

    <a role="menuitem" class="dropdown-item" href="https://docs.github.com" data-ga-click="Header, go to help, text:help" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;HELP&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="092cfb6c41e690eb134f68920b95eabbad12307ca217fe7acf72db50731cb5f3" >Help</a>
    <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;SETTINGS&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="5b4ed834c0f0c583158b2a576d56825bf776eabca09b07898d8ab1a864e24c8a" >Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="X6okWnLmJcNbfLM+eblaARX5bpHM9PFBBS6LRZUNLeRD3vLz2HIz6x77JjkEdM0JaUq7o9Suys6QHBzHFdnpZg==" />
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" data-hydro-click="{&quot;event_type&quot;:&quot;global_header.user_menu_dropdown.click&quot;,&quot;payload&quot;:{&quot;request_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;target&quot;:&quot;SIGN_OUT&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="7439e982ac44190eb2744e34f08a401e22547428214952551882e20cb2728d1c"  role="menuitem">
        Sign out
      </button>
      <input type="text" name="required_field_da30" hidden="hidden" class="form-control" /><input type="hidden" name="timestamp" value="1601236420248" class="form-control" /><input type="hidden" name="timestamp_secret" value="dc31271cfa6f2bd45ab18fad7f0ee9979e3122f1258d5ed9880155240f9553cd" class="form-control" />
</form>  </details-menu>
</details>

    </div>
</header>

          

    </div>

  <div id="start-of-content" class="show-on-focus"></div>






    <div id="js-flash-container">


  <template class="js-flash-template">
    <div class="flash flash-full  {{ className }}">
  <div class=" px-2" >
    <button class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
    </button>
    
      <div>{{ message }}</div>

  </div>
</div>
  </template>
</div>


  

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>



  <div
    class="application-main "
    data-commit-hovercards-enabled
    data-discussion-hovercards-enabled
    data-issue-and-pr-hovercards-enabled
  >
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      

    






  


  <div class="bg-gray-light pt-3 hide-full-screen mb-5">

      <div class="d-flex mb-3 px-3 px-md-4 px-lg-5">

        <div class="flex-auto min-width-0 width-fit mr-3">
            <h1 class=" d-flex flex-wrap flex-items-center break-word f3 text-normal">
    <svg class="octicon octicon-repo text-gray" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
  <span class="author ml-2 flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/BurnySc2/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/BurnySc2">BurnySc2</a>
  </span>
  <span class="mx-1 flex-self-stretch">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#js-repo-pjax-container" href="/BurnySc2/python-sc2">python-sc2</a>
  </strong>
  
</h1>


        </div>

          <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">

  <li>
            <form data-remote="true" class="d-flex js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="Y3hsy3hTt8hbqPMbc366UtFrvWobUPDeuMAg/tUVkrFDmzlor/fsvGYHdYGdMpEQ8aluBUTD281nUKd4NyqtJQ==" />      <input type="hidden" name="repository_id" value="188820422">

      <details class="details-reset details-overlay select-menu hx_rsm">
        <summary class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:188820422,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="90fa788e45db3ed2e26ead84d349c60bf64872091e6b4ac89a7c963726d6f9b3" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg height="16" class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path></svg>
              Watch
          </span>
          <span class="dropdown-caret"></span>
</summary>        <details-menu
          class="select-menu-modal position-absolute mt-5"
          style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg height="16" class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg height="16" class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.679 7.932c.412-.621 1.242-1.75 2.366-2.717C5.175 4.242 6.527 3.5 8 3.5c1.473 0 2.824.742 3.955 1.715 1.124.967 1.954 2.096 2.366 2.717a.119.119 0 010 .136c-.412.621-1.242 1.75-2.366 2.717C10.825 11.758 9.473 12.5 8 12.5c-1.473 0-2.824-.742-3.955-1.715C2.92 9.818 2.09 8.69 1.679 8.068a.119.119 0 010-.136zM8 2c-1.981 0-3.67.992-4.933 2.078C1.797 5.169.88 6.423.43 7.1a1.619 1.619 0 000 1.798c.45.678 1.367 1.932 2.637 3.024C4.329 13.008 6.019 14 8 14c1.981 0 3.67-.992 4.933-2.078 1.27-1.091 2.187-2.345 2.637-3.023a1.619 1.619 0 000-1.798c-.45-.678-1.367-1.932-2.637-3.023C11.671 2.992 9.981 2 8 2zm0 8a2 2 0 100-4 2 2 0 000 4z"></path></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" height="16" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg height="16" class="octicon octicon-bell-slash" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5c-.997 0-1.895.416-2.534 1.086A.75.75 0 014.38 1.55 5 5 0 0113 5v2.373a.75.75 0 01-1.5 0V5A3.5 3.5 0 008 1.5zM4.182 4.31L1.19 2.143a.75.75 0 10-.88 1.214L3 5.305v2.642a.25.25 0 01-.042.139L1.255 10.64A1.518 1.518 0 002.518 13h11.108l1.184.857a.75.75 0 10.88-1.214l-1.375-.996a1.196 1.196 0 00-.013-.01L4.198 4.321a.733.733 0 00-.016-.011zm7.373 7.19L4.5 6.391v1.556c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01.015.015 0 00.005.012.017.017 0 00.006.004l.007.001h9.037zM8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count"
          href="/BurnySc2/python-sc2/watchers"
          aria-label="10 users are watching this repository">
          10
        </a>
</form>
  </li>

  <li>
        <div class="js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="/BurnySc2/python-sc2/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="9NW6XYQVWkF10cHFPR2F5F/TjdO3lEyFqAYhnlPYBDSXy2UHwxS853FfR0ugqE3HNohYGw6t0UHdUDKJD2qVCg==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count  js-toggler-target" aria-label="Unstar this repository" title="Unstar BurnySc2/python-sc2" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:188820422,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="84c46b0ee7225ec61358c3c51f7c3120f85da54aa899514eb8bf661ec31f6a3e" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg height="16" class="octicon octicon-star-fill" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"></path></svg>
        Unstar
</button>        <a class="social-count js-social-count" href="/BurnySc2/python-sc2/stargazers"
           aria-label="102 users starred this repository">
           102
        </a>
</form>
    <form class="unstarred js-social-form" action="/BurnySc2/python-sc2/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="lTjTbN1P+cX1yJBE1WhFoIIwtrrL2v8tSOGrPUDwLfx9ZD9QnloIDaYJfZ/6/q4r4jUQUUKd3tsBzjM8uw75uQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count  js-toggler-target" aria-label="Unstar this repository" title="Star BurnySc2/python-sc2" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:188820422,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="9001daca0bc48588759ebaade51ac3aed8e21dc8b16f69430bbd34d5a8f12010" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg height="16" class="octicon octicon-star" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path></svg>
        Star
</button>        <a class="social-count js-social-count" href="/BurnySc2/python-sc2/stargazers"
           aria-label="102 users starred this repository">
          102
        </a>
</form>  </div>

  </li>

  <li>
            <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/BurnySc2/python-sc2/fork" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="i3hye93r90P1EbNbEZqTsooUV/5sZUOM8NObdZfPm/+bQSBN9P0pl412A6nkGT9xSQcY+gu+tfDEfBk7YucanA==" />
              <button class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:188820422,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="7ef4973ca386d54754a9cbf43e561f33108b85e77069a1fd2f0b9212b7f09c86" data-ga-click="Repository, show fork modal, action:blob#show; text:Fork" type="submit" title="Fork your own copy of BurnySc2/python-sc2 to your account" aria-label="Fork your own copy of BurnySc2/python-sc2 to your account">                <svg class="octicon octicon-repo-forked" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path></svg>
                Fork
</button></form>
      <a href="/BurnySc2/python-sc2/network/members" class="social-count"
         aria-label="36 users forked this repository">
        36
      </a>
  </li>
</ul>

      </div>
        
<nav aria-label="Repository" data-pjax="#js-repo-pjax-container" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5 bg-gray-light">
  <ul class="UnderlineNav-body list-style-none ">
          <li class="d-flex">
        <a class="js-selected-navigation-item selected UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="code-tab" data-hotkey="g c" data-ga-click="Repository, Navigation click, Code tab" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /BurnySc2/python-sc2" href="/BurnySc2/python-sc2">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path></svg>
            <span data-content="Code">Code</span>
              <span title="Not available" class="Counter "></span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="issues-tab" data-hotkey="g i" data-ga-click="Repository, Navigation click, Issues tab" data-selected-links="repo_issues repo_labels repo_milestones /BurnySc2/python-sc2/issues" href="/BurnySc2/python-sc2/issues">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z"></path></svg>
            <span data-content="Issues">Issues</span>
              <span title="11" class="Counter ">11</span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="pull-requests-tab" data-hotkey="g p" data-ga-click="Repository, Navigation click, Pull requests tab" data-selected-links="repo_pulls checks /BurnySc2/python-sc2/pulls" href="/BurnySc2/python-sc2/pulls">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path></svg>
            <span data-content="Pull requests">Pull requests</span>
              <span title="0" hidden="hidden" class="Counter ">0</span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="actions-tab" data-hotkey="g a" data-ga-click="Repository, Navigation click, Actions tab" data-selected-links="repo_actions /BurnySc2/python-sc2/actions" href="/BurnySc2/python-sc2/actions">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"></path></svg>
            <span data-content="Actions">Actions</span>
              <span title="Not available" class="Counter "></span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="projects-tab" data-hotkey="g b" data-ga-click="Repository, Navigation click, Projects tab" data-selected-links="repo_projects new_repo_project repo_project /BurnySc2/python-sc2/projects" href="/BurnySc2/python-sc2/projects">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-project UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
            <span data-content="Projects">Projects</span>
              <span title="0" hidden="hidden" class="Counter ">0</span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="wiki-tab" data-hotkey="g w" data-ga-click="Repository, Navigation click, Wikis tab" data-selected-links="repo_wiki /BurnySc2/python-sc2/wiki" href="/BurnySc2/python-sc2/wiki">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-book UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 1.75A.75.75 0 01.75 1h4.253c1.227 0 2.317.59 3 1.501A3.744 3.744 0 0111.006 1h4.245a.75.75 0 01.75.75v10.5a.75.75 0 01-.75.75h-4.507a2.25 2.25 0 00-1.591.659l-.622.621a.75.75 0 01-1.06 0l-.622-.621A2.25 2.25 0 005.258 13H.75a.75.75 0 01-.75-.75V1.75zm8.755 3a2.25 2.25 0 012.25-2.25H14.5v9h-3.757c-.71 0-1.4.201-1.992.572l.004-7.322zm-1.504 7.324l.004-5.073-.002-2.253A2.25 2.25 0 005.003 2.5H1.5v9h3.757a3.75 3.75 0 011.994.574z"></path></svg>
            <span data-content="Wiki">Wiki</span>
              <span title="Not available" class="Counter "></span>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="security-tab" data-hotkey="g s" data-ga-click="Repository, Navigation click, Security tab" data-selected-links="security overview alerts policy token_scanning code_scanning /BurnySc2/python-sc2/security" href="/BurnySc2/python-sc2/security">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z"></path></svg>
            <span data-content="Security">Security</span>
              <include-fragment src="/BurnySc2/python-sc2/security/overall-count" accept="text/fragment+html"></include-fragment>
</a>      </li>
      <li class="d-flex">
        <a class="js-selected-navigation-item UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item" data-tab-item="insights-tab" data-ga-click="Repository, Navigation click, Insights tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people /BurnySc2/python-sc2/pulse" href="/BurnySc2/python-sc2/pulse">
              <svg classes="UnderlineNav-octicon" display="none inline" height="16" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z"></path></svg>
            <span data-content="Insights">Insights</span>
              <span title="Not available" class="Counter "></span>
</a>      </li>

</ul>        <div class="position-absolute right-0 pr-3 pr-md-4 pr-lg-5 js-responsive-underlinenav-overflow" style="visibility:hidden;">
      <details class="details-overlay details-reset position-relative">
  <summary role="button">
    <div class="UnderlineNav-item mr-0 border-0">
            <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg>
            <span class="sr-only">More</span>
          </div>
</summary>  <div>
    <details-menu role="menu" class="dropdown-menu dropdown-menu-sw ">
  
            <ul>
                <li data-menu-item="code-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /BurnySc2/python-sc2" href="/BurnySc2/python-sc2">
                    Code
</a>                </li>
                <li data-menu-item="issues-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /BurnySc2/python-sc2/issues" href="/BurnySc2/python-sc2/issues">
                    Issues
</a>                </li>
                <li data-menu-item="pull-requests-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /BurnySc2/python-sc2/pulls" href="/BurnySc2/python-sc2/pulls">
                    Pull requests
</a>                </li>
                <li data-menu-item="actions-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /BurnySc2/python-sc2/actions" href="/BurnySc2/python-sc2/actions">
                    Actions
</a>                </li>
                <li data-menu-item="projects-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /BurnySc2/python-sc2/projects" href="/BurnySc2/python-sc2/projects">
                    Projects
</a>                </li>
                <li data-menu-item="wiki-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /BurnySc2/python-sc2/wiki" href="/BurnySc2/python-sc2/wiki">
                    Wiki
</a>                </li>
                <li data-menu-item="security-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /BurnySc2/python-sc2/security" href="/BurnySc2/python-sc2/security">
                    Security
</a>                </li>
                <li data-menu-item="insights-tab" hidden>
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links=" /BurnySc2/python-sc2/pulse" href="/BurnySc2/python-sc2/pulse">
                    Insights
</a>                </li>
            </ul>

</details-menu>
</div></details>    </div>

</nav>
  </div>

<div class="container-xl clearfix new-discussion-timeline px-3 px-md-4 px-lg-5">
  <div class="repository-content " >

    
      
  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/BurnySc2/python-sc2/blob/69f08c5f6f81632939760b642996cea012d5612a/examples/terran/onebase_battlecruiser.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v22:79fb6417c0c09b60f2dcf522c0f24f82e614c5c0313ca2efffeab6a75197131b -->
    

    <div class="d-flex flex-items-start flex-shrink-0 pb-3 flex-wrap flex-md-nowrap flex-justify-between flex-md-justify-start">
      
<div class="position-relative">
  <details class="details-reset details-overlay mr-0 mb-0 " id="branch-select-menu">
    <summary class="btn css-truncate"
            data-hotkey="w"
            title="Switch branches or tags">
      <svg text="gray" height="16" class="octicon octicon-git-branch text-gray" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path></svg>
      <span class="css-truncate-target" data-menu-button>develop</span>
      <span class="dropdown-caret"></span>
    </summary>

    <details-menu class="SelectMenu SelectMenu--hasFilter" src="/BurnySc2/python-sc2/refs/develop/examples/terran/onebase_battlecruiser.py?source_action=show&amp;source_controller=blob" preload>
      <div class="SelectMenu-modal">
        <include-fragment class="SelectMenu-loading" aria-label="Menu is loading">
          <svg class="octicon octicon-octoface anim-pulse" height="32" viewBox="0 0 24 24" version="1.1" width="32" aria-hidden="true"><path d="M7.75 11c-.69 0-1.25.56-1.25 1.25v1.5a1.25 1.25 0 102.5 0v-1.5C9 11.56 8.44 11 7.75 11zm1.27 4.5a.469.469 0 01.48-.5h5a.47.47 0 01.48.5c-.116 1.316-.759 2.5-2.98 2.5s-2.864-1.184-2.98-2.5zm7.23-4.5c-.69 0-1.25.56-1.25 1.25v1.5a1.25 1.25 0 102.5 0v-1.5c0-.69-.56-1.25-1.25-1.25z"></path><path fill-rule="evenodd" d="M21.255 3.82a1.725 1.725 0 00-2.141-1.195c-.557.16-1.406.44-2.264.866-.78.386-1.647.93-2.293 1.677A18.442 18.442 0 0012 5c-.93 0-1.784.059-2.569.17-.645-.74-1.505-1.28-2.28-1.664a13.876 13.876 0 00-2.265-.866 1.725 1.725 0 00-2.141 1.196 23.645 23.645 0 00-.69 3.292c-.125.97-.191 2.07-.066 3.112C1.254 11.882 1 13.734 1 15.527 1 19.915 3.13 23 12 23c8.87 0 11-3.053 11-7.473 0-1.794-.255-3.647-.99-5.29.127-1.046.06-2.15-.066-3.125a23.652 23.652 0 00-.689-3.292zM20.5 14c.5 3.5-1.5 6.5-8.5 6.5s-9-3-8.5-6.5c.583-4 3-6 8.5-6s7.928 2 8.5 6z"></path></svg>
        </include-fragment>
      </div>
    </details-menu>
  </details>

</div>

      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal mx-0 mx-md-3 width-full width-md-auto flex-order-1 flex-md-order-none mt-3 mt-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/BurnySc2/python-sc2"><span>python-sc2</span></a></span></span><span class="separator">/</span><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/BurnySc2/python-sc2/tree/develop/examples"><span>examples</span></a></span><span class="separator">/</span><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/BurnySc2/python-sc2/tree/develop/examples/terran"><span>terran</span></a></span><span class="separator">/</span><strong class="final-path">onebase_battlecruiser.py</strong>
          <span class="separator">/</span><details class="details-reset details-overlay d-inline" id="jumpto-symbol-select-menu">
  <summary class="btn-link link-gray css-truncate" aria-haspopup="true" data-hotkey="r" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_blob_definitions&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_blob_definitions&quot;,&quot;repository_id&quot;:188820422,&quot;ref&quot;:&quot;develop&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="e97f86b6c7bacea0bc02893c7bb4cd5b307eb06d3c0e937f9b645a8a44d63615">
      <svg class="octicon octicon-code" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path></svg>
    <span data-menu-button>Jump to</span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="SelectMenu SelectMenu--hasFilter" role="menu">
    <div class="SelectMenu-modal">
      <header class="SelectMenu-header">
        <span class="SelectMenu-title">Code definitions</span>
        <button class="SelectMenu-closeButton" type="button" data-toggle-for="jumpto-symbol-select-menu">
          <svg aria-label="Close menu" class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" role="img"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
        </button>
      </header>
        <div class="SelectMenu-filter">
          <input
            class="SelectMenu-input form-control js-filterable-field"
            id="jumpto-symbols-filter-field"
            type="text"
            autocomplete="off"
            spellcheck="false"
            autofocus
            placeholder="Filter definitions"
            aria-label="Filter definitions">
        </div>
      <div class="SelectMenu-list">
        <div data-filterable-for="jumpto-symbols-filter-field" data-filterable-type="substring">
            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:188820422,&quot;ref&quot;:&quot;develop&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="dce1abd20f460044b2e16a5b86daa9587e779c3471f4b5190169c42dc9272d8f" href="/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py#L18">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>BCRushBot</span>
              <span class="flex-auto d-flex flex-justify-end">Class</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:188820422,&quot;ref&quot;:&quot;develop&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="dce1abd20f460044b2e16a5b86daa9587e779c3471f4b5190169c42dc9272d8f" href="/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py#L19">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>select_target</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:188820422,&quot;ref&quot;:&quot;develop&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="dce1abd20f460044b2e16a5b86daa9587e779c3471f4b5190169c42dc9272d8f" href="/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py#L34">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>on_step</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:188820422,&quot;ref&quot;:&quot;develop&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="dce1abd20f460044b2e16a5b86daa9587e779c3471f4b5190169c42dc9272d8f" href="/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py#L116">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>starport_points_to_build_addon</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:188820422,&quot;ref&quot;:&quot;develop&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="dce1abd20f460044b2e16a5b86daa9587e779c3471f4b5190169c42dc9272d8f" href="/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py#L140">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>starport_land_positions</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:188820422,&quot;ref&quot;:&quot;develop&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="dce1abd20f460044b2e16a5b86daa9587e779c3471f4b5190169c42dc9272d8f" href="/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py#L186">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>main</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>        </div>
      </div>
      <footer class="SelectMenu-footer">
        <div class="d-flex flex-justify-between">
          Code navigation index up-to-date
          <svg class="octicon octicon-dot-fill text-green" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path></svg>
        </div>
      </footer>
    </div>
  </details-menu>
</details>

      </h2>
      <a href="/BurnySc2/python-sc2/find/develop"
            class="js-pjax-capture-input btn mr-2 d-none d-md-block"
            data-pjax
            data-hotkey="t">
        Go to file
      </a>

      <details id="blob-more-options-details" class="details-overlay details-reset position-relative">
  <summary role="button">
    <svg aria-label="More options" height="16" class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" version="1.1" width="16" role="img"><path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg>
</summary>  <div>
    <ul class="dropdown-menu dropdown-menu-sw">
            <li class="d-block d-md-none">
              <a class="dropdown-item d-flex flex-items-baseline" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FIND_FILE_BUTTON&quot;,&quot;repository_id&quot;:188820422,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}" data-hydro-click-hmac="a2914cf25903fb06c1c26039df927c75d5f867728429a4269a38be5518781d5d" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" data-pjax="true" href="/BurnySc2/python-sc2/find/develop">
                <span class="flex-auto">Go to file</span>
                <span class="text-small text-gray" aria-hidden="true">T</span>
</a>            </li>
            <li data-toggle-for="blob-more-options-details">
              <button type="button" data-toggle-for="jumpto-line-details-dialog" class="btn-link dropdown-item">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Go to line</span>
                  <span class="text-small text-gray" aria-hidden="true">L</span>
                </span>
              </button>
            </li>
            <li data-toggle-for="blob-more-options-details">
              <button type="button" data-toggle-for="jumpto-symbol-select-menu" class="btn-link dropdown-item">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Go to definition</span>
                  <span class="text-small text-gray" aria-hidden="true">R</span>
                </span>
              </button>
            </li>
            <li class="dropdown-divider" role="none"></li>
            <li>
              <clipboard-copy value="examples/terran/onebase_battlecruiser.py" class="dropdown-item cursor-pointer" data-toggle-for="blob-more-options-details">
                Copy path
              </clipboard-copy>
            </li>
          </ul>
</div></details>    </div>



    <div class="Box d-flex flex-column flex-shrink-0 mb-3">
      
  <div class="Box-header Box-header--blue Details js-details-container">
      <div class="d-flex flex-items-center">
        <span class="flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1">
          <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/users/BurnySc2/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/BurnySc2"><img class="avatar avatar-user" src="https://avatars2.githubusercontent.com/u/21288725?s=48&amp;v=4" width="24" height="24" alt="@BurnySc2" /></a>
        </span>
        <div class="flex-1 d-flex flex-items-center ml-3 min-width-0">
          <div class="css-truncate css-truncate-overflow">
            <a class="text-bold link-gray-dark" rel="author" data-hovercard-type="user" data-hovercard-url="/users/BurnySc2/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/BurnySc2">BurnySc2</a>

              <span>
                <a data-pjax="true" title="Fix hydra and BC bots" class="link-gray" href="/BurnySc2/python-sc2/commit/446ee108926fc9869e8fec71973a1598e410c09d">Fix hydra and BC bots</a>
              </span>
          </div>


          <span class="ml-2">
            <include-fragment accept="text/fragment+html" src="/BurnySc2/python-sc2/commit/446ee108926fc9869e8fec71973a1598e410c09d/rollup?direction=e" class="d-inline"></include-fragment>
          </span>
        </div>
        <div class="ml-3 d-flex flex-shrink-0 flex-items-center flex-justify-end text-gray no-wrap">
          <span class="d-none d-md-inline">
            <span>Latest commit</span>
            <a class="text-small text-mono link-gray" href="/BurnySc2/python-sc2/commit/446ee108926fc9869e8fec71973a1598e410c09d" data-pjax>446ee10</a>
            <span itemprop="dateModified"><relative-time datetime="2020-04-02T17:06:23Z" class="no-wrap">Apr 2, 2020</relative-time></span>
          </span>

          <a data-pjax href="/BurnySc2/python-sc2/commits/develop/examples/terran/onebase_battlecruiser.py" class="ml-3 no-wrap link-gray-dark no-underline">
            <svg text="gray" height="16" class="octicon octicon-history text-gray" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"></path></svg>
            <span class="d-none d-sm-inline">
              <strong>History</strong>
            </span>
          </a>
        </div>
      </div>

  </div>

  <div class="Box-body d-flex flex-items-center flex-auto border-bottom-0 flex-wrap" >
    <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-3" id="blob_contributors_box">
      <summary class="link-gray-dark">
        <svg text="gray" height="16" class="octicon octicon-people text-gray" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416.672v.352a.75.75 0 00.574.73c1.2.289 2.162 1.2 2.522 2.372a.75.75 0 101.434-.44 5.01 5.01 0 00-2.56-3.012A3 3 0 0011 4z"></path></svg>
        <strong>4</strong>
        
        contributors
      </summary>
      <details-dialog
        class="Box Box--overlay d-flex flex-column anim-fade-in fast"
        aria-label="Users who have contributed to this file"
        src="/BurnySc2/python-sc2/contributors-list/develop/examples/terran/onebase_battlecruiser.py" preload>
        <div class="Box-header">
          <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
          </button>
          <h3 class="Box-title">
            Users who have contributed to this file
          </h3>
        </div>
        <include-fragment class="octocat-spinner my-3" aria-label="Loading..."></include-fragment>
      </details-dialog>
    </details>
      <span class="">
    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/users/BurnySc2/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/BurnySc2/python-sc2/commits/develop/examples/terran/onebase_battlecruiser.py?author=BurnySc2">
      <img class="avatar mr-2 avatar-user" src="https://avatars2.githubusercontent.com/u/21288725?s=48&amp;v=4" width="24" height="24" alt="@BurnySc2" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/users/tweakimp/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/BurnySc2/python-sc2/commits/develop/examples/terran/onebase_battlecruiser.py?author=tweakimp">
      <img class="avatar mr-2 avatar-user" src="https://avatars1.githubusercontent.com/u/20489521?s=48&amp;v=4" width="24" height="24" alt="@tweakimp" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/users/Matuiss2/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/BurnySc2/python-sc2/commits/develop/examples/terran/onebase_battlecruiser.py?author=Matuiss2">
      <img class="avatar mr-2 avatar-user" src="https://avatars1.githubusercontent.com/u/31539494?s=48&amp;v=4" width="24" height="24" alt="@Matuiss2" /> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/users/Dentosal/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/BurnySc2/python-sc2/commits/develop/examples/terran/onebase_battlecruiser.py?author=Dentosal">
      <img class="avatar mr-2 avatar-user" src="https://avatars3.githubusercontent.com/u/2204863?s=48&amp;v=4" width="24" height="24" alt="@Dentosal" /> 
</a>
</span>

  </div>
    </div>






    <div class="Box mt-3 position-relative
      ">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">
  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">

      199 lines (169 sloc)
      <span class="file-info-divider"></span>
    8.8 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a href="/BurnySc2/python-sc2/raw/develop/examples/terran/onebase_battlecruiser.py" id="raw-url" role="button" class="btn btn-sm BtnGroup-item ">Raw</a>
        <a href="/BurnySc2/python-sc2/blame/develop/examples/terran/onebase_battlecruiser.py" data-hotkey="b" role="button" class="btn js-update-url-with-hash btn-sm BtnGroup-item ">Blame</a>
    </div>

    <div>
          <a class="btn-octicon tooltipped tooltipped-nw js-remove-unless-platform"
             data-platforms="windows,mac"
             href="x-github-client://openRepo/https://github.com/BurnySc2/python-sc2?branch=develop&amp;filepath=examples%2Fterran%2Fonebase_battlecruiser.py"
             aria-label="Open this file in GitHub Desktop"
             data-ga-click="Repository, open with desktop">
              <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.75 2.5h12.5a.25.25 0 01.25.25v7.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25v-7.5a.25.25 0 01.25-.25zM14.25 1H1.75A1.75 1.75 0 000 2.75v7.5C0 11.216.784 12 1.75 12h3.727c-.1 1.041-.52 1.872-1.292 2.757A.75.75 0 004.75 16h6.5a.75.75 0 00.565-1.243c-.772-.885-1.193-1.716-1.292-2.757h3.727A1.75 1.75 0 0016 10.25v-7.5A1.75 1.75 0 0014.25 1zM9.018 12H6.982a5.72 5.72 0 01-.765 2.5h3.566a5.72 5.72 0 01-.765-2.5z"></path></svg>
          </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/BurnySc2/python-sc2/edit/develop/examples/terran/onebase_battlecruiser.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="+CIMO6nzOzrL6sr0JjoMDaeTWnCcSjJ9wtOieUimAN03N76t7IsrIGfycW0ij7YCEI+HJvupare1cz71EuaupA==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM11.189 6.25L9.75 4.81l-6.286 6.287a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.249.249 0 00.108-.064l6.286-6.286z"></path></svg>
            </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/BurnySc2/python-sc2/delete/develop/examples/terran/onebase_battlecruiser.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="ulIMPNrZDpjAu4SM5Mi0cZsL5qKnb13AsF8wiINgkTzTtIbitX2zGMQOIIC8AITvT57I/uo0i/ZBABRJ+STtpg==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and delete the file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path></svg>
            </button>
</form>    </div>
  </div>
</div>



      

  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python  gist-border-0">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8" data-paste-markdown-skip>
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>sys</span>, <span class=pl-s1>os</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>sys</span>.<span class=pl-s1>path</span>.<span class=pl-en>append</span>(<span class=pl-s1>os</span>.<span class=pl-s1>path</span>.<span class=pl-en>join</span>(<span class=pl-s1>os</span>.<span class=pl-s1>path</span>.<span class=pl-en>dirname</span>(<span class=pl-s1>__file__</span>), <span class=pl-s>&quot;../..&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>typing</span> <span class=pl-k>import</span> <span class=pl-v>Tuple</span>, <span class=pl-v>List</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>sc2</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sc2</span> <span class=pl-k>import</span> <span class=pl-v>Race</span>, <span class=pl-v>Difficulty</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sc2</span>.<span class=pl-s1>constants</span> <span class=pl-k>import</span> <span class=pl-c1>*</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sc2</span>.<span class=pl-s1>player</span> <span class=pl-k>import</span> <span class=pl-v>Bot</span>, <span class=pl-v>Computer</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sc2</span>.<span class=pl-s1>player</span> <span class=pl-k>import</span> <span class=pl-v>Human</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sc2</span>.<span class=pl-s1>unit</span> <span class=pl-k>import</span> <span class=pl-v>Unit</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sc2</span>.<span class=pl-s1>units</span> <span class=pl-k>import</span> <span class=pl-v>Units</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sc2</span>.<span class=pl-s1>position</span> <span class=pl-k>import</span> <span class=pl-v>Point2</span>, <span class=pl-v>Point3</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sc2</span>.<span class=pl-s1>ids</span>.<span class=pl-s1>unit_typeid</span> <span class=pl-k>import</span> <span class=pl-v>UnitTypeId</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>BCRushBot</span>(<span class=pl-s1>sc2</span>.<span class=pl-v>BotAI</span>):</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>select_target</span>(<span class=pl-s1>self</span>) <span class=pl-c1>-&gt;</span> <span class=pl-v>Tuple</span>[<span class=pl-v>Point2</span>, <span class=pl-s1>bool</span>]:</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot; Select an enemy target the units should attack. &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>targets</span>: <span class=pl-v>Units</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>enemy_structures</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>targets</span>:</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span> <span class=pl-s1>targets</span>.<span class=pl-s1>random</span>.<span class=pl-s1>position</span>, <span class=pl-c1>True</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>targets</span>: <span class=pl-v>Units</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>enemy_units</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>targets</span>:</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span> <span class=pl-s1>targets</span>.<span class=pl-s1>random</span>.<span class=pl-s1>position</span>, <span class=pl-c1>True</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>units</span> <span class=pl-c1>and</span> <span class=pl-en>min</span>([<span class=pl-s1>u</span>.<span class=pl-s1>position</span>.<span class=pl-en>distance_to</span>(<span class=pl-s1>self</span>.<span class=pl-s1>enemy_start_locations</span>[<span class=pl-c1>0</span>]) <span class=pl-k>for</span> <span class=pl-s1>u</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>units</span>]) <span class=pl-c1>&lt;</span> <span class=pl-c1>5</span>:</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>enemy_start_locations</span>[<span class=pl-c1>0</span>].<span class=pl-s1>position</span>, <span class=pl-c1>False</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>mineral_field</span>.<span class=pl-s1>random</span>.<span class=pl-s1>position</span>, <span class=pl-c1>False</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>async</span> <span class=pl-k>def</span> <span class=pl-en>on_step</span>(<span class=pl-s1>self</span>, <span class=pl-s1>iteration</span>):</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ccs</span>: <span class=pl-v>Units</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>townhalls</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># If we no longer have townhalls, attack with all workers</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>ccs</span>:</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>target</span>, <span class=pl-s1>target_is_enemy_unit</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>select_target</span>()</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>unit</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>workers</span> <span class=pl-c1>|</span> <span class=pl-s1>self</span>.<span class=pl-en>units</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BATTLECRUISER</span>):</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>unit</span>.<span class=pl-s1>is_attacking</span>:</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>unit</span>.<span class=pl-en>attack</span>(<span class=pl-s1>target</span>)</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>cc</span>: <span class=pl-v>Unit</span> <span class=pl-c1>=</span> <span class=pl-s1>ccs</span>.<span class=pl-s1>random</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Send all BCs to attack a target.</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>bcs</span>: <span class=pl-v>Units</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>units</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BATTLECRUISER</span>)</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>bcs</span>:</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>target</span>, <span class=pl-s1>target_is_enemy_unit</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>select_target</span>()</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>bc</span>: <span class=pl-v>Unit</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>bc</span> <span class=pl-c1>in</span> <span class=pl-s1>bcs</span>:</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># Order the BC to attack-move the target</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>target_is_enemy_unit</span> <span class=pl-c1>and</span> (<span class=pl-s1>bc</span>.<span class=pl-s1>is_idle</span> <span class=pl-c1>or</span> <span class=pl-s1>bc</span>.<span class=pl-s1>is_moving</span>):</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>bc</span>.<span class=pl-en>attack</span>(<span class=pl-s1>target</span>)</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># Order the BC to move to the target, and once the select_target returns an attack-target, change it to attack-move</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>elif</span> <span class=pl-s1>bc</span>.<span class=pl-s1>is_idle</span>:</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>bc</span>.<span class=pl-en>move</span>(<span class=pl-s1>target</span>)</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Build more SCVs until 22</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>SCV</span>) <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-s1>supply_workers</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>22</span> <span class=pl-c1>and</span> <span class=pl-s1>cc</span>.<span class=pl-s1>is_idle</span>:</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>cc</span>.<span class=pl-en>train</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>SCV</span>)</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Build more BCs</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>FUSIONCORE</span>) <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BATTLECRUISER</span>):</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>sp</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORT</span>).<span class=pl-s1>idle</span>:</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>sp</span>.<span class=pl-s1>has_add_on</span>:</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BATTLECRUISER</span>):</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>sp</span>.<span class=pl-en>train</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BATTLECRUISER</span>)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Build more supply depots</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>supply_left</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>6</span> <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-s1>supply_used</span> <span class=pl-c1>&gt;=</span> <span class=pl-c1>14</span> <span class=pl-c1>and</span> <span class=pl-c1>not</span> <span class=pl-s1>self</span>.<span class=pl-en>already_pending</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>SUPPLYDEPOT</span>):</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>SUPPLYDEPOT</span>):</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>await</span> <span class=pl-s1>self</span>.<span class=pl-en>build</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>SUPPLYDEPOT</span>, <span class=pl-s1>near</span><span class=pl-c1>=</span><span class=pl-s1>cc</span>.<span class=pl-s1>position</span>.<span class=pl-en>towards</span>(<span class=pl-s1>self</span>.<span class=pl-s1>game_info</span>.<span class=pl-s1>map_center</span>, <span class=pl-c1>8</span>))</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Build barracks if we have none</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>tech_requirement_progress</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BARRACKS</span>) <span class=pl-c1>==</span> <span class=pl-c1>1</span>:</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BARRACKS</span>):</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BARRACKS</span>):</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>await</span> <span class=pl-s1>self</span>.<span class=pl-en>build</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BARRACKS</span>, <span class=pl-s1>near</span><span class=pl-c1>=</span><span class=pl-s1>cc</span>.<span class=pl-s1>position</span>.<span class=pl-en>towards</span>(<span class=pl-s1>self</span>.<span class=pl-s1>game_info</span>.<span class=pl-s1>map_center</span>, <span class=pl-c1>8</span>))</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># Build refineries</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>BARRACKS</span>) <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-s1>gas_buildings</span>.<span class=pl-s1>amount</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>2</span>:</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>REFINERY</span>):</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>vgs</span>: <span class=pl-v>Units</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>vespene_geyser</span>.<span class=pl-en>closer_than</span>(<span class=pl-c1>20</span>, <span class=pl-s1>cc</span>)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>for</span> <span class=pl-s1>vg</span> <span class=pl-c1>in</span> <span class=pl-s1>vgs</span>:</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>gas_buildings</span>.<span class=pl-en>filter</span>(<span class=pl-k>lambda</span> <span class=pl-s1>unit</span>: <span class=pl-s1>unit</span>.<span class=pl-en>distance_to</span>(<span class=pl-s1>vg</span>) <span class=pl-c1>&lt;</span> <span class=pl-c1>1</span>):</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">                            <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">                        <span class=pl-s1>worker</span>: <span class=pl-v>Unit</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>select_build_worker</span>(<span class=pl-s1>vg</span>.<span class=pl-s1>position</span>)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>if</span> <span class=pl-s1>worker</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">                            <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">                        <span class=pl-s1>worker</span>.<span class=pl-en>build</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>REFINERY</span>, <span class=pl-s1>vg</span>)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># Build factory if we dont have one</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>tech_requirement_progress</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>FACTORY</span>) <span class=pl-c1>==</span> <span class=pl-c1>1</span>:</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>factories</span>: <span class=pl-v>Units</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>FACTORY</span>)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>factories</span>:</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>FACTORY</span>):</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>await</span> <span class=pl-s1>self</span>.<span class=pl-en>build</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>FACTORY</span>, <span class=pl-s1>near</span><span class=pl-c1>=</span><span class=pl-s1>cc</span>.<span class=pl-s1>position</span>.<span class=pl-en>towards</span>(<span class=pl-s1>self</span>.<span class=pl-s1>game_info</span>.<span class=pl-s1>map_center</span>, <span class=pl-c1>8</span>))</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># Build starport once we can build starports, up to 2</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>elif</span> (</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>factories</span>.<span class=pl-s1>ready</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">                    <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-s1>structures</span>.<span class=pl-en>of_type</span>({<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORT</span>, <span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORTFLYING</span>}).<span class=pl-s1>ready</span>.<span class=pl-s1>amount</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">                    <span class=pl-c1>+</span> <span class=pl-s1>self</span>.<span class=pl-en>already_pending</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORT</span>)</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">                    <span class=pl-c1>&lt;</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">                ):</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORT</span>):</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>await</span> <span class=pl-s1>self</span>.<span class=pl-en>build</span>(</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">                            <span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORT</span>,</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">                            <span class=pl-s1>near</span><span class=pl-c1>=</span><span class=pl-s1>cc</span>.<span class=pl-s1>position</span>.<span class=pl-en>towards</span>(<span class=pl-s1>self</span>.<span class=pl-s1>game_info</span>.<span class=pl-s1>map_center</span>, <span class=pl-c1>15</span>).<span class=pl-en>random_on_distance</span>(<span class=pl-c1>8</span>),</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">                        )</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>def</span> <span class=pl-en>starport_points_to_build_addon</span>(<span class=pl-s1>sp_position</span>: <span class=pl-v>Point2</span>) <span class=pl-c1>-&gt;</span> <span class=pl-v>List</span>[<span class=pl-v>Point2</span>]:</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;&quot;&quot; Return all points that need to be checked when trying to build an addon. Returns 4 points. &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>addon_offset</span>: <span class=pl-v>Point2</span> <span class=pl-c1>=</span> <span class=pl-v>Point2</span>((<span class=pl-c1>2.5</span>, <span class=pl-c1>-</span><span class=pl-c1>0.5</span>))</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>addon_position</span>: <span class=pl-v>Point2</span> <span class=pl-c1>=</span> <span class=pl-s1>sp_position</span> <span class=pl-c1>+</span> <span class=pl-s1>addon_offset</span></td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>addon_points</span> <span class=pl-c1>=</span> [</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">                (<span class=pl-s1>addon_position</span> <span class=pl-c1>+</span> <span class=pl-v>Point2</span>((<span class=pl-s1>x</span> <span class=pl-c1>-</span> <span class=pl-c1>0.5</span>, <span class=pl-s1>y</span> <span class=pl-c1>-</span> <span class=pl-c1>0.5</span>))).<span class=pl-s1>rounded</span> <span class=pl-k>for</span> <span class=pl-s1>x</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-c1>0</span>, <span class=pl-c1>2</span>) <span class=pl-k>for</span> <span class=pl-s1>y</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-c1>0</span>, <span class=pl-c1>2</span>)</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">            ]</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span> <span class=pl-s1>addon_points</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Build starport techlab or lift if no room to build techlab</span></td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>sp</span>: <span class=pl-v>Unit</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>sp</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORT</span>).<span class=pl-s1>ready</span>.<span class=pl-s1>idle</span>:</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>sp</span>.<span class=pl-s1>has_add_on</span> <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORTTECHLAB</span>):</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>addon_points</span> <span class=pl-c1>=</span> <span class=pl-en>starport_points_to_build_addon</span>(<span class=pl-s1>sp</span>.<span class=pl-s1>position</span>)</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-en>all</span>(</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-en>in_map_bounds</span>(<span class=pl-s1>addon_point</span>)</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">                    <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-en>in_placement_grid</span>(<span class=pl-s1>addon_point</span>)</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">                    <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-en>in_pathing_grid</span>(<span class=pl-s1>addon_point</span>)</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>for</span> <span class=pl-s1>addon_point</span> <span class=pl-c1>in</span> <span class=pl-s1>addon_points</span></td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">                ):</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>sp</span>.<span class=pl-en>build</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORTTECHLAB</span>)</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">                    <span class=pl-en>sp</span>(<span class=pl-v>AbilityId</span>.<span class=pl-v>LIFT</span>)</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>def</span> <span class=pl-en>starport_land_positions</span>(<span class=pl-s1>sp_position</span>: <span class=pl-v>Point2</span>) <span class=pl-c1>-&gt;</span> <span class=pl-v>List</span>[<span class=pl-v>Point2</span>]:</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;&quot;&quot; Return all points that need to be checked when trying to land at a location where there is enough space to build an addon. Returns 13 points. &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>land_positions</span> <span class=pl-c1>=</span> [(<span class=pl-s1>sp_position</span> <span class=pl-c1>+</span> <span class=pl-v>Point2</span>((<span class=pl-s1>x</span>, <span class=pl-s1>y</span>))).<span class=pl-s1>rounded</span> <span class=pl-k>for</span> <span class=pl-s1>x</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-c1>-</span><span class=pl-c1>1</span>, <span class=pl-c1>2</span>) <span class=pl-k>for</span> <span class=pl-s1>y</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-c1>-</span><span class=pl-c1>1</span>, <span class=pl-c1>2</span>)]</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span> <span class=pl-s1>land_positions</span> <span class=pl-c1>+</span> <span class=pl-en>starport_points_to_build_addon</span>(<span class=pl-s1>sp_position</span>)</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Find a position to land for a flying starport so that it can build an addon</span></td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>sp</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORTFLYING</span>).<span class=pl-s1>idle</span>:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>possible_land_positions_offset</span> <span class=pl-c1>=</span> <span class=pl-en>sorted</span>(</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">                (<span class=pl-v>Point2</span>((<span class=pl-s1>x</span>, <span class=pl-s1>y</span>)) <span class=pl-k>for</span> <span class=pl-s1>x</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-c1>-</span><span class=pl-c1>10</span>, <span class=pl-c1>10</span>) <span class=pl-k>for</span> <span class=pl-s1>y</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-c1>-</span><span class=pl-c1>10</span>, <span class=pl-c1>10</span>)),</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>key</span><span class=pl-c1>=</span><span class=pl-k>lambda</span> <span class=pl-s1>point</span>: <span class=pl-s1>point</span>.<span class=pl-s1>x</span> <span class=pl-c1>**</span> <span class=pl-c1>2</span> <span class=pl-c1>+</span> <span class=pl-s1>point</span>.<span class=pl-s1>y</span> <span class=pl-c1>**</span> <span class=pl-c1>2</span>,</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>offset_point</span>: <span class=pl-v>Point2</span> <span class=pl-c1>=</span> <span class=pl-v>Point2</span>((<span class=pl-c1>-</span><span class=pl-c1>0.5</span>, <span class=pl-c1>-</span><span class=pl-c1>0.5</span>))</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>possible_land_positions</span> <span class=pl-c1>=</span> (<span class=pl-s1>sp</span>.<span class=pl-s1>position</span>.<span class=pl-s1>rounded</span> <span class=pl-c1>+</span> <span class=pl-s1>offset_point</span> <span class=pl-c1>+</span> <span class=pl-s1>p</span> <span class=pl-k>for</span> <span class=pl-s1>p</span> <span class=pl-c1>in</span> <span class=pl-s1>possible_land_positions_offset</span>)</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>target_land_position</span> <span class=pl-c1>in</span> <span class=pl-s1>possible_land_positions</span>:</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>land_and_addon_points</span>: <span class=pl-v>List</span>[<span class=pl-v>Point2</span>] <span class=pl-c1>=</span> <span class=pl-en>starport_land_positions</span>(<span class=pl-s1>target_land_position</span>)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-en>all</span>(</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-en>in_map_bounds</span>(<span class=pl-s1>land_pos</span>) <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-en>in_placement_grid</span>(<span class=pl-s1>land_pos</span>) <span class=pl-c1>and</span> <span class=pl-s1>self</span>.<span class=pl-en>in_pathing_grid</span>(<span class=pl-s1>land_pos</span>)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>for</span> <span class=pl-s1>land_pos</span> <span class=pl-c1>in</span> <span class=pl-s1>land_and_addon_points</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">                ):</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">                    <span class=pl-en>sp</span>(<span class=pl-v>AbilityId</span>.<span class=pl-v>LAND</span>, <span class=pl-s1>target_land_position</span>)</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Show where it is flying to and show grid</span></td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>unit</span>: <span class=pl-v>Unit</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>sp</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORTFLYING</span>).<span class=pl-en>filter</span>(<span class=pl-k>lambda</span> <span class=pl-s1>unit</span>: <span class=pl-c1>not</span> <span class=pl-s1>unit</span>.<span class=pl-s1>is_idle</span>):</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-en>isinstance</span>(<span class=pl-s1>sp</span>.<span class=pl-s1>order_target</span>, <span class=pl-v>Point2</span>):</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>p</span>: <span class=pl-v>Point3</span> <span class=pl-c1>=</span> <span class=pl-v>Point3</span>((<span class=pl-c1>*</span><span class=pl-s1>sp</span>.<span class=pl-s1>order_target</span>, <span class=pl-s1>self</span>.<span class=pl-en>get_terrain_z_height</span>(<span class=pl-s1>sp</span>.<span class=pl-s1>order_target</span>)))</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>client</span>.<span class=pl-en>debug_box2_out</span>(<span class=pl-s1>p</span>, <span class=pl-s1>color</span><span class=pl-c1>=</span><span class=pl-v>Point3</span>((<span class=pl-c1>255</span>, <span class=pl-c1>0</span>, <span class=pl-c1>0</span>)))</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Build fusion core</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>STARPORT</span>).<span class=pl-s1>ready</span>:</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>can_afford</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>FUSIONCORE</span>) <span class=pl-c1>and</span> <span class=pl-c1>not</span> <span class=pl-s1>self</span>.<span class=pl-en>structures</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>FUSIONCORE</span>):</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>await</span> <span class=pl-s1>self</span>.<span class=pl-en>build</span>(<span class=pl-v>UnitTypeId</span>.<span class=pl-v>FUSIONCORE</span>, <span class=pl-s1>near</span><span class=pl-c1>=</span><span class=pl-s1>cc</span>.<span class=pl-s1>position</span>.<span class=pl-en>towards</span>(<span class=pl-s1>self</span>.<span class=pl-s1>game_info</span>.<span class=pl-s1>map_center</span>, <span class=pl-c1>8</span>))</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Saturate refineries</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>refinery</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>gas_buildings</span>:</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>refinery</span>.<span class=pl-s1>assigned_harvesters</span> <span class=pl-c1>&lt;</span> <span class=pl-s1>refinery</span>.<span class=pl-s1>ideal_harvesters</span>:</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>worker</span>: <span class=pl-v>Units</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>workers</span>.<span class=pl-en>closer_than</span>(<span class=pl-c1>10</span>, <span class=pl-s1>refinery</span>)</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>worker</span>:</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>worker</span>.<span class=pl-s1>random</span>.<span class=pl-en>gather</span>(<span class=pl-s1>refinery</span>)</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Send workers back to mine if they are idle</span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>scv</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>workers</span>.<span class=pl-s1>idle</span>:</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>scv</span>.<span class=pl-en>gather</span>(<span class=pl-s1>self</span>.<span class=pl-s1>mineral_field</span>.<span class=pl-en>closest_to</span>(<span class=pl-s1>cc</span>))</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line"><span class=pl-k>def</span> <span class=pl-en>main</span>():</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>sc2</span>.<span class=pl-en>run_game</span>(</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>sc2</span>.<span class=pl-s1>maps</span>.<span class=pl-en>get</span>(<span class=pl-s>&quot;(2)CatalystLE&quot;</span>),</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">        [</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># Human(Race.Terran),</span></td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">            <span class=pl-v>Bot</span>(<span class=pl-v>Race</span>.<span class=pl-v>Terran</span>, <span class=pl-v>BCRushBot</span>()),</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">            <span class=pl-v>Computer</span>(<span class=pl-v>Race</span>.<span class=pl-v>Zerg</span>, <span class=pl-v>Difficulty</span>.<span class=pl-v>Hard</span>),</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">        ],</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>realtime</span><span class=pl-c1>=</span><span class=pl-c1>False</span>,</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">    )</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line"><span class=pl-k>if</span> <span class=pl-s1>__name__</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;__main__&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">    <span class=pl-en>main</span>()</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/BurnySc2/python-sc2/blame/69f08c5f6f81632939760b642996cea012d5612a/examples/terran/onebase_battlecruiser.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/BurnySc2/python-sc2/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  


  <details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/BurnySc2/python-sc2/find-definition"
     data-tagsearch-ref="develop"
     data-tagsearch-path="examples/terran/onebase_battlecruiser.py"
     data-tagsearch-lang="Python"
     data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:188820422,&quot;ref&quot;:&quot;develop&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/BurnySc2/python-sc2/blob/develop/examples/terran/onebase_battlecruiser.py&quot;,&quot;user_id&quot;:55979445}}"
     data-hydro-click-hmac="5dcae49cdd2201cfd4a89bb05f8020082bead93a49c62a6befaa002764d3d346">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>




  </div>
</div>

    </main>
  </div>

  </div>

        
<div class="footer container-xl width-full p-responsive" role="contentinfo">
    <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
      <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
          <li><a data-ga-click="Footer, go to help, text:help" href="https://docs.github.com">Help</a></li>
      </ul>

      <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
        <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
      <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
          <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://services.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
          <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
          <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
      </ul>
    </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" async="async" integrity="sha512-bn/3rKJzBl2H64K38R8KaVcT26vKK7BJQC59lwYc+9fjlHzmy0fwh+hzBtsgTdhIi13dxjzNKWhdSN8WTM9qUw==" type="application/javascript" id="js-conditional-compat" data-src="https://github.githubassets.com/assets/compat-bootstrap-6e7ff7ac.js"></script>
    <script crossorigin="anonymous" integrity="sha512-CxjaMepCmi+z0LTeztU2S8qGD25LyHD6j9t0RSPevy63trFWJVwUM6ipAVLgtpMBBgZ53wq8JPkSeQ6ruaZL2w==" type="application/javascript" src="https://github.githubassets.com/assets/environment-bootstrap-0b18da31.js"></script>
    <script crossorigin="anonymous" async="async" integrity="sha512-0AXkWwkiw45XIvngmWo/0uryDdhd0Hur2YAUCEdd5+gYDVQb4ymn5FQkIBpMa5uoQybM3qSRdA04eqo8A35B7Q==" type="application/javascript" src="https://github.githubassets.com/assets/vendor-d005e45b.js"></script>
    <script crossorigin="anonymous" async="async" integrity="sha512-MImAWI8TKrFFO937djwu2lEmJWi7eavNSWzFs0Kd/feV7W38estgTLCGahlhMtUu9MZ5LuWtQ46LM6qxHJqPQw==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-30898058.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-5hcZPkyv7o5YO8ckKMKsNWmOm8eVmyHkCL9XKfhdCiW3K8sROU4nyH5jPspTtg1xwgfHYvR7l5ZiG8kkq01+Hw==" type="application/javascript" src="https://github.githubassets.com/assets/behaviors-bootstrap-e617193e.js"></script>
    
      <script crossorigin="anonymous" async="async" integrity="sha512-WmLHdpvEzC/gyDbs4RKm2+pVCCIDmiJ4vPW5zdX6lQN1CxH/gYnRSi0gyMHMJv5Xv7zUbD6vOgwlAO6yNI87Vg==" type="application/javascript" data-module-id="./contributions-spider-graph.js" data-src="https://github.githubassets.com/assets/contributions-spider-graph-5a62c776.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-2tVomjR7M73FMhb8dUvdjjzAErhNyLB9tL++hwpJeElQv494sCpS8OnWZL981ktAg30aqIypXD6TJjdvxcPEWQ==" type="application/javascript" data-module-id="./drag-drop.js" data-src="https://github.githubassets.com/assets/drag-drop-dad5689a.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-6E3ph805JNUrG/ivkdXS6lJPW99Ze7JlLusPAp2t035OQd+7AjD4X6g5hioZwPU1yFxczoNKdEKytmWgLp7WYw==" type="application/javascript" data-module-id="./jump-to.js" data-src="https://github.githubassets.com/assets/jump-to-e84de987.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-O5MUDplY2zVCSB3Jq0MiMf/lhuo8NBywywSaMZnViWL4ynNrhfhtn1LtGMfqYvyPP3BlHsq3Qli2a1ei19IqsQ==" type="application/javascript" data-module-id="./manage-membership.js" data-src="https://github.githubassets.com/assets/manage-membership-bootstrap-3b93140e.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-e14YmKeE7DtBVONbVv52sO9Sp56BRExkstaqtgYIAu3xlMNtMEXI2//4NqDn+THjxv49R/cobZ7cv8KFF6mspw==" type="application/javascript" data-module-id="./profile-pins-element.js" data-src="https://github.githubassets.com/assets/profile-pins-element-7b5e1898.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-JXSmOrOQXof4xz7y+engxtqrugUopipC5LwEmsfxit4PlVe48UECBUCLuujjIADm1kjb2f/9/azX+qNspSy90w==" type="application/javascript" data-module-id="./randomColor.js" data-src="https://github.githubassets.com/assets/randomColor-2574a63a.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-FOUgzyCYz3T1et4Stcl3MeKUX3mZkQcsMsTQDgBj6/CtW3HrwyGMaCeXGyhSjTGibphNptgZKgDNkvL+O+2uYw==" type="application/javascript" data-module-id="./sortable-behavior.js" data-src="https://github.githubassets.com/assets/sortable-behavior-14e520cf.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-Sqqua2FOZToK8Mzg1e4jBubR6ZCFO0gL2JHjgpqafLawUXr69ffELu+IhApoX5uhWlxXxJ0ooE89ANBMtWiUNA==" type="application/javascript" data-module-id="./tweetsodium.js" data-src="https://github.githubassets.com/assets/tweetsodium-4aaaae6b.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-3Q6/aKl7PXjI+jB+sUpF8+h/c+m0WOOTiExsBCxtrmhCgQX5kVWx1SA7LuELWaK0EjS4SNffZcXJMbs0hbqx8w==" type="application/javascript" data-module-id="./user-status-submit.js" data-src="https://github.githubassets.com/assets/user-status-submit-dd0ebf68.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-/qScxtjexP2u3QkKCuwrz5nBriYatgocp4bz+lKaWT2CfpZjON9ZtcjoJi8gvOTrSiWP8tD2yoXZ82R5W2UssQ==" type="application/javascript" src="https://github.githubassets.com/assets/repositories-bootstrap-fea49cc6.js"></script>
<script crossorigin="anonymous" async="async" integrity="sha512-4uQvKBaDHwwOtxkHrpFSW7T3ag6D4e9kAykpUagCtVeN9lyhnicMf5ABWbS57QNmhtFayornB8HuUIs805G5tQ==" type="application/javascript" src="https://github.githubassets.com/assets/diffs-bootstrap-e2e42f28.js"></script>
<script crossorigin="anonymous" async="async" integrity="sha512-2iOlkD8iyiXXmuWQIJPgs5fKKEUgQT+StG9y7v8yXsBOeHM2lcM1xu7e4GldRoDt50fTc5tIIL/Zu76YIWog/w==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-da23a590.js"></script>
  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>


  </body>
</html>

