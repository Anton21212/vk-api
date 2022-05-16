from ..error import *


def error_checker(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        if 'response' in result:
            print("OK")
        elif result['error']['error_code'] == 214:
            raise AccessToAddingPostDenied
        elif result['error']['error_code'] == 1:
            raise UnknownErrorHasOccurred
        elif result['error']['error_code'] == 2:
            raise TheApplicationIsDisabled
        elif result['error']['error_code'] == 3:
            raise UnknownMethodPassed
        elif result['error']['error_code'] == 4:
            raise InvalidSignature
        elif result['error']['error_code'] == 5:
            raise UserAuthorizationFailed
        elif result['error']['error_code'] == 6:
            raise TooManyRequestsPerSecond
        elif result['error']['error_code'] == 7:
            raise YouDoNotHavePermissionToPerformThisAction
        elif result['error']['error_code'] == 8:
            raise InvalidRequest
        elif result['error']['error_code'] == 9:
            raise TooManySimilarActions
        elif result['error']['error_code'] == 10:
            raise AnInternalServerErrorHasOccurred
        elif result['error']['error_code'] == 11:
            raise InTestModeTheApplicationMustBeTurnedOffOrTheUserMustBeLoggedIn
        elif result['error']['error_code'] == 14:
            raise YouNeedToEnterTheCodeFromTheImageCaptcha
        elif result['error']['error_code'] == 15:
            raise AccessIsDenied
        elif result['error']['error_code'] == 16:
            raise RequestsMustBeMadeOverHTTPSBecauseTheUserHasEnabledASettingThatRequiresWorkOverASecureConnection
        elif result['error']['error_code'] == 17:
            raise UserValidationRequired
        elif result['error']['error_code'] == 18:
            raise ThePageHasBeenRemovedOrBlocked
        elif result['error']['error_code'] == 19:
            raise ContentBlocked
        elif result['error']['error_code'] == 20:
            raise ThisActionIsProhibitedForNonStandaloneApplications
        elif result['error']['error_code'] == 21:
            raise ThisActionIsAllowedOnlyForStandaloneAndOpenAPIApplications
        elif result['error']['error_code'] == 23:
            raise TheMethodHasBeenDisabled
        elif result['error']['error_code'] == 24:
            raise UserConfirmationRequired
        elif result['error']['error_code'] == 27:
            raise TheCommunityAccessKeyIsInvalid
        elif result['error']['error_code'] == 28:
            raise TheApplicationAccessKeyIsInvalid
        elif result['error']['error_code'] == 29:
            raise QuantityLimitPerMethodCallReached
        elif result['error']['error_code'] == 30:
            raise ProfileIsPrivate
        elif result['error']['error_code'] == 100:
            raise OneOfTheRequiredParametersWasNotPassedOrIsInvalid
        elif result['error']['error_code'] == 101:
            raise InvalidApplicationAPIID
        elif result['error']['error_code'] == 113:
            raise InvalidUserID
        elif result['error']['error_code'] == 150:
            raise InvalidTimestamp
        elif result['error']['error_code'] == 200:
            raise AlbumAccessDenied
        elif result['error']['error_code'] == 201:
            raise AudioAccessDenied
        elif result['error']['error_code'] == 203:
            raise GroupAccessDenied
        elif result['error']['error_code'] == 210:
            raise AccessToWallsPostDenied
        elif result['error']['error_code'] == 211:
            raise AccessToWallsCommentDenied
        elif result['error']['error_code'] == 212:
            raise AccessToPostCommentsDenied
        elif result['error']['error_code'] == 213:
            raise AccessToStatusRepliesDenied
        elif result['error']['error_code'] == 219:
            raise AdvertisementPostWasRecentlyAdded
        elif result['error']['error_code'] == 220:
            raise TooManyRecipients
        elif result['error']['error_code'] == 222:
            raise HyperlinksAreForbidden
        elif result['error']['error_code'] == 223:
            raise TooManyReplies
        elif result['error']['error_code'] == 224:
            raise TooManyAdsPosts
        elif result['error']['error_code'] == 225:
            raise DonutIsDisabled
        elif result['error']['error_code'] == 300:
            raise AlbumFull
        elif result['error']['error_code'] == 500:
            raise ActionDeniedYouMustEnableVoiceTranslationsInTheAppSettings
        elif result['error']['error_code'] == 600:
            raise NoRightsToPerformTheseOperationsWithTheAdvertisingAccount
        elif result['error']['error_code'] == 603:
            raise AnErrorOccurredWhileWorkingWithTheAdvertisingAccount
        elif result['error']['error_code'] == 3102:
            raise SpecifiedLinkIsIncorrectCantFindSource

        return result

    return wrapper
