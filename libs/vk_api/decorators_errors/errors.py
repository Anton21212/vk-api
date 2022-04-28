from libs.vk_api.exceptions import *


def decorator(func):
    def inner(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        if result['error']['error_code'] == 1:
            raise UnknownErrorHasOccurred
        if result['error']['error_code'] == 2:
            raise TheApplicationIsDisabled
        if result['error']['error_code'] == 3:
            raise UnknownMethodPassed
        if result['error']['error_code'] == 4:
            raise InvalidSignature
        if result['error']['error_code'] == 5:
            raise UserAuthorizationFailed
        if result['error']['error_code'] == 6:
            raise TooManyRequestsPerSecond
        if result['error']['error_code'] == 7:
            raise YouDoNotHavePermissionToPerformThisAction
        if result['error']['error_code'] == 8:
            raise InvalidRequest
        if result['error']['error_code'] == 9:
            raise TooManySimilarActions
        if result['error']['error_code'] == 10:
            raise AnInternalServerErrorHasOccurred
        if result['error']['error_code'] == 11:
            raise InTestModeTheApplicationMustBeTurnedOffOrTheUserMustBeLoggedIn
        if result['error']['error_code'] == 14:
            raise YouNeedToEnterTheCodeFromTheImageCaptcha
        if result['error']['error_code'] == 15:
            raise AccessIsDenied
        if result['error']['error_code'] == 16:
            raise RequestsMustBeMadeOverHTTPSBecauseTheUserHasEnabledASettingThatRequiresWorkOverASecureConnection
        if result['error']['error_code'] == 17:
            raise UserValidationRequired
        if result['error']['error_code'] == 18:
            raise ThePageHasBeenRemovedOrBlocked
        if result['error']['error_code'] == 19:
            raise ContentBlocked
        if result['error']['error_code'] == 20:
            raise ThisActionIsProhibitedForNonStandaloneApplications
        if result['error']['error_code'] == 21:
            raise ThisActionIsAllowedOnlyForStandaloneAndOpenAPIApplications
        if result['error']['error_code'] == 23:
            raise TheMethodHasBeenDisabled
        if result['error']['error_code'] == 24:
            raise UserConfirmationRequired
        if result['error']['error_code'] == 27:
            raise TheCommunityAccessKeyIsInvalid
        if result['error']['error_code'] == 28:
            raise TheApplicationAccessKeyIsInvalid
        if result['error']['error_code'] == 29:
            raise QuantityLimitPerMethodCallReached
        if result['error']['error_code'] == 30:
            raise ProfileIsPrivate
        if result['error']['error_code'] == 100:
            raise OneOfTheRequiredParametersWasNotPassedOrIsInvalid
        if result['error']['error_code'] == 101:
            raise InvalidApplicationAPIID
        if result['error']['error_code'] == 113:
            raise InvalidUserID
        if result['error']['error_code'] == 150:
            raise InvalidTimestamp
        if result['error']['error_code'] == 200:
            raise AlbumAccessDenied
        if result['error']['error_code'] == 201:
            raise AudioAccessDenied
        if result['error']['error_code'] == 203:
            raise GroupAccessDenied
        if result['error']['error_code'] == 210:
            raise AccessToWallsPostDenied
        if result['error']['error_code'] == 211:
            raise AccessToWallsCommentDenied
        if result['error']['error_code'] == 212:
            raise AccessToPostCommentsDenied
        if result['error']['error_code'] == 213:
            raise AccessToStatusRepliesDenied
        if result['error']['error_code'] == 214:
            raise AccessToAddingPostDenied
        if result['error']['error_code'] == 219:
            raise AdvertisementPostWasRecentlyAdded
        if result['error']['error_code'] == 220:
            raise TooManyRecipients
        if result['error']['error_code'] == 222:
            raise HyperlinksAreForbidden
        if result['error']['error_code'] == 223:
            raise TooManyReplies
        if result['error']['error_code'] == 224:
            raise TooManyAdsPosts
        if result['error']['error_code'] == 225:
            raise DonutIsDisabled
        if result['error']['error_code'] == 300:
            raise AlbumFull
        if result['error']['error_code'] == 500:
            raise ActionDeniedYouMustEnableVoiceTranslationsInTheAppSettings
        if result['error']['error_code'] == 600:
            raise NoRightsToPerformTheseOperationsWithTheAdvertisingAccount
        if result['error']['error_code'] == 603:
            raise AnErrorOccurredWhileWorkingWithTheAdvertisingAccount
        if result['error']['error_code'] == 3102:
            raise SpecifiedLinkIsIncorrectCantFindSource

        print("Finish")

    return inner
