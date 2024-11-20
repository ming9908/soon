import { ScrollViewStyleReset } from 'expo-router/html';
import { type PropsWithChildren } from 'react';

/**
 * This file is web-only and used to configure the root HTML for every web page during static rendering.
 * The contents of this function only run in Node.js environments and do not have access to the DOM or browser APIs.
 */
export default function Root({ children }: PropsWithChildren) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <link href="https://hangeul.pstatic.net/hangeul_static/css/nanum-gothic-coding.css" rel="stylesheet"></link>
        <link href="https://hangeul.pstatic.net/hangeul_static/css/nanum-barun-gothic.css" rel="stylesheet"></link>
        <link rel="preconnect" href="https://fonts.googleapis.com"></link>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin></link>
        <link href="https://fonts.googleapis.com/css2?family=Itim&display=swap" rel="stylesheet"></link>
        {/*
          Disable body scrolling on web. This makes ScrollView components work closer to how they do on native.
          However, body scrolling is often nice to have for mobile web. If you want to enable it, remove this line.
        */}
        <ScrollViewStyleReset />

        {/* Using raw CSS styles as an escape-hatch to ensure the background color never flickers in dark-mode. */}
        <style dangerouslySetInnerHTML={{ __html: responsiveBackground }} />
        {/* Add any additional <head> elements that you want globally available on web... */}
      </head>
      <body>{children}</body>
    </html>
  );
}

const responsiveBackground = `
body {
  background-color: #fff;
  font-family: 'NanumBarunGothic';
  -ms-overflow-style: none; /* 인터넷 익스플로러 */
  scrollbar-width: none; /* 파이어폭스 */
}
@media (prefers-color-scheme: dark) {
  body {
    background-color: #000;
  }
}
::-webkit-scrollbar {
  display: none;
}
`;
/*
// font-family: 'NanumGothicCodingLigature';
// font-family: 'NanumGothicCodingLigatureBold';
// font-family: 'NanumGothicCoding';
// font-family: 'NanumGothicCodingBold';
// font-family: 'NanumBarunGothicUltraLight';
// font-family: 'NanumBarunGothicLight';
// font-family: 'NanumBarunGothic';
// font-family: 'NanumBarunGothicBold';
*/