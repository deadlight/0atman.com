Title: Publishing Vanilla
Category: Coding
Status: draft
Summary: Being a description on how we publish our CSS framework at Canonical
Tags: canonical, ubuntu, node, scss


We've got a new CSS framework at Canonical, named [Vanilla](http://ubuntudesign.github.io/vanilla-framework/). My colleague [Ant](http://design.canonical.com/author/ya-bo-ng/) has a great write-up [introducing Vanilla](http://design.canonical.com/2015/06/introducing-vanilla/). Essentially it's a CSS microframework powered by scss. The build process consists of two steps.

### Open Source Build
We wanted the build to be as automated and close to CI/CD principles as possible. Here's what happens:

Committing to our [github repository](https://github.com/ubuntudesign/vanilla-framework) kicks off a travis build that runs gulp tests, which include [sasslint](https://github.com/brigade/scss-lint/). And we also use [david-dm.org](https://david-dm.org/ubuntudesign/vanilla-framework#info=devDependencies) to make sure our npm dependencies are up to date. Both of these have nice badges we can link to right from our github page, so the first thing people see is the heath of our project. I really like this, it keeps us honest.

Not everything can be done with travis, however, as publishing Vanilla to [npm](https://www.npmjs.com/), updating our project page and demo site require some private credentials. For the confidential build, we use [Jenkins](https://jenkins-ci.org/). (formally Hudson).

### Private Build with Jenkins
Our Jenkins build does a few things:

0. Increment the package.json version number
0. npm publish
0. Build sass with `npm install`
0. Upload styles.css to our assets server
0. Update sassdoc
0. Update demo site with new CSS


[Robin](http://design.canonical.com/author/nottrobin/) put this functionality together in a neat script: [publish.sh](https://github.com/ubuntudesign/vanilla-builder/blob/master/publish.sh).

We use this script in a Jenkins build that we kick off with a few parameters, `point`, `minor` and `major` to indicate the version to be updated in package.json. This allows our devs push-button releases on the fly.

After less than 30 seconds, our [demo site](http://ubuntudesign.github.io/vanilla-framework/demo/), which showcases our `elements?` and their usage, is updated. This demo is styled with the latest version of Vanilla, and also serves as documentation and a test of the CSS.

### The Future
It'd be nice for the demo test (which we currently just eyeball) to be automated, perhaps with a visual diff tool such as [PhantomCSS](https://github.com/Huddle/PhantomCSS) or a bespoke solution with Selenium.

### Wrap-up
Vanilla is ready to hack on, go get it [here](http://design.canonical.com/2015/06/introducing-vanilla/) and tell us what you think! (And yes, you can get it in colours other than _Ubuntu Orange_)
