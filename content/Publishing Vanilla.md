Title: Publishing Vanilla
Category: Coding
Status: draft
Summary: Being a description on how we publish our css framework at Canonical
Tags: canonical, ubuntu, node, scss


## Edit scss
Here at Canonical, we have recently but together a scss framework, as mentioned by [Ant](http://design.canonical.com/author/ya-bo-ng/) [here](http://design.canonical.com/2015/06/introducing-vanilla/).

## Build
Commiting to our [github repository](https://github.com/ubuntudesign/vanilla-framework) kicks off a travis build that runs out gulp tests, which include [sasslint](https://github.com/brigade/scss-lint/).
and we also use [david-dm.org](https://david-dm.org/ubuntudesign/vanilla-framework#info=devDependencies) to make sure our npm dependencies are fresh.

## jenkins build
Our jenkins build does a few things:

0. update package.json (Increment the package.js version number)
0. npm publish
0. build sass with `npm install`
0. upload styles.css to our assets server
0. update sassdoc
0. update demo site with new css


[Robin](http://design.canonical.com/author/nottrobin/) put this functionality together in a neat script: [publish.sh](https://github.com/ubuntudesign/vanilla-builder/blob/master/publish.sh).

We use this script in a jenkins build that we kick off with a few parameters, `point`, `minor` and `major` to indicate the version to be updated in package.json.

After less than 30 seconds, our [demo site](http://ubuntudesign.github.io/vanilla-framework/demo/), which showcases our `elements?` and their usage.
